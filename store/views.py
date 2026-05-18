from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})

def about(request):
    return render(request, 'store/about.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'store/login.html')
