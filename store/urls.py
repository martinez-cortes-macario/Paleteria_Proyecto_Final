from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.product_list, name='products'),
    path('producto/<int:id>/', views.product_detail, name='product_detail'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),

    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('success/', views.success, name='success'),
]

