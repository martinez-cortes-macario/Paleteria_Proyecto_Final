from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.product_list, name='products'),
    path('producto/<int:id>/', views.product_detail, name='product_detail'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
]

