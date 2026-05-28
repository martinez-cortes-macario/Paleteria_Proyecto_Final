from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

def home(request):

    query = request.GET.get('q')

    if query:
        paletas = Product.objects.filter(
            categoria__nombre="Paletas",
            name__icontains=query
        )

        nieves = Product.objects.filter(
            categoria__nombre="Nieves",
            name__icontains=query
        )

        aguas = Product.objects.filter(
            categoria__nombre="Aguas",
            name__icontains=query
        )

        snacks = Product.objects.filter(
            categoria__nombre="Snacks",
            name__icontains=query
        )

    else:
        paletas = Product.objects.filter(categoria__nombre="Paletas")
        nieves = Product.objects.filter(categoria__nombre="Nieves")
        aguas = Product.objects.filter(categoria__nombre="Aguas")
        snacks = Product.objects.filter(categoria__nombre="Snacks")

    context = {
        'paletas': paletas,
        'nieves': nieves,
        'aguas': aguas,
        'snacks': snacks,
    }

    return render(request, 'store/home.html', context)
def product_list(request):

    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'store/products.html', {
        'products': products
    })

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
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product = get_object_or_404(Product, id=product_id)

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('cart')


def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product.quantity = quantity
        product.subtotal = product.price * quantity
        total += product.subtotal
        products.append(product)

    return render(request, 'store/cart.html', {
        'products': products,
        'total': total
    })


def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')


def success(request):
    request.session['cart'] = {}
    return render(request, 'store/success.html')

def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'store/register.html')


def logout_view(request):
    logout(request)
    return redirect('home')