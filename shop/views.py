from rest_framework import viewsets, permissions, status, serializers  # Add serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart, CartItem, Order, Review
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer, OrderSerializer, ReviewSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.http import JsonResponse
from .models import Product

# API Views
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        product_id = self.request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        if not Order.objects.filter(user=self.request.user, status='completed').exists():
            raise serializers.ValidationError("You must purchase this product to review it.")
        serializer.save(user=self.request.user, product=product)

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return Response({'status': 'item added to cart'})

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart = get_object_or_404(Cart, user=self.request.user)
        total_amount = sum(item.product.price * item.quantity for item in cart.items.all())
        serializer.save(user=self.request.user, total_amount=total_amount)
        cart.items.all().delete()

# Template Views
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

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product, defaults={'quantity': quantity}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    messages.success(request, 'Item added to cart!')
    return redirect('product_list')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    total_amount = sum(item.product.price * item.quantity for item in cart.items.all())
    return render(request, 'cart_detail.html', {'cart': cart, 'total_amount': total_amount})

@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    total_amount = sum(item.product.price * item.quantity for item in cart.items.all())
    if total_amount > 0:
        Order.objects.create(user=request.user, total_amount=total_amount, status='completed')
        cart.items.all().delete()
        messages.success(request, 'Order placed successfully!')
    return redirect('order_list')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not Order.objects.filter(user=request.user, status='completed').exists():
        messages.error(request, 'You must purchase a product to review it.')
        return redirect('product_detail', product_id=product.id)
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment', '')
        Review.objects.create(user=request.user, product=product, rating=rating, comment=comment)
        messages.success(request, 'Review submitted!')
    return redirect('product_detail', product_id=product.id)


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
    