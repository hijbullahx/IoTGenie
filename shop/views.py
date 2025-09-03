from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from rest_framework import viewsets
from .models import Product, Cart, CartItem, Order, OrderItem
from .serializers import ProductSerializer, CartSerializer, OrderSerializer
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import logging

logger = logging.getLogger(__name__)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def product_list(request):
    products = Product.objects.all()
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )
    if category_filter:
        products = products.filter(category=category_filter)

    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.view_count += 1
    product.save()
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        if not item_created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, f"{product.name} (x{quantity}) added to cart!")
    else:
        messages.error(request, "Invalid quantity.")
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_amount = sum(item.total_price for item in cart.items.all())
    return render(request, 'cart_detail.html', {'cart': cart, 'total_amount': total_amount})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f"{product_name} removed from cart!")
    return redirect('cart_detail')

@login_required
def purchase_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        messages.error(request, "Your cart is empty!")
        return redirect('cart_detail')
    total_amount = sum(item.total_price for item in cart.items.all())
    return render(request, 'purchase_order.html', {'cart': cart, 'total_amount': total_amount})

@login_required
def place_order(request):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        if not cart.items.exists():
            messages.error(request, "Your cart is empty!")
            return redirect('cart_detail')
        total_amount = sum(item.total_price for item in cart.items.all())
        # Get next order number for this user
        last_order = Order.objects.filter(user=request.user).order_by('-user_order_number').first()
        next_order_number = (last_order.user_order_number + 1) if last_order else 1
        order = Order.objects.create(
            user=request.user,
            total_amount=total_amount,
            user_order_number=next_order_number
        )
        logger.info(f"Order #{order.user_order_number} (ID: {order.id}) created for user {request.user.username}")
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart.items.all().delete()
        messages.success(request, "Order placed successfully! Payment gateway integration pending.")
        return redirect('order_list')
    return redirect('cart_detail')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    logger.info(f"Fetching orders for user {request.user.username}: {orders.count()} orders found")
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def cancel_order_item(request, order_id, item_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_item = get_object_or_404(OrderItem, id=item_id, order=order)
    product_name = order_item.product.name
    order_item.delete()
    logger.info(f"OrderItem {item_id} removed from Order #{order.user_order_number} (ID: {order.id}) for user {request.user.username}")
    remaining_items = order.items.all()
    if remaining_items.exists():
        order.total_amount = sum(item.total_price for item in remaining_items)
        order.save()
        messages.success(request, f"{product_name} removed from Order #{order.user_order_number}!")
    else:
        order_number = order.user_order_number
        order.delete()
        messages.success(request, f"Order #{order_number} is removed.")
    return redirect('order_list')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Registration successful!')
        return super().form_valid(form)

def product_search_suggestions(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query).values('id', 'name')[:5]
        suggestions = [{'id': p['id'], 'name': p['name']} for p in products]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            if password_form.cleaned_data.get('new_password1'):
                password_form.save()
                update_session_auth_hash(request, request.user)
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserProfileForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })