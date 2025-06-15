from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'carts', views.CartViewSet, basename='cart')
router.register(r'orders', views.OrderViewSet, basename='order')

urlpatterns = [
    path('', lambda request: redirect('product_list'), name='home'),
    path('api/', include(router.urls)),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/purchase/', views.purchase_order, name='purchase_order'),
    path('orders/place/', views.place_order, name='place_order'),
    path('orders/cancel/<int:order_id>/<int:item_id>/', views.cancel_order_item, name='cancel_order_item'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api/suggestions/', views.product_search_suggestions, name='product_search_suggestions'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]