from django.shortcuts import render, redirect
from .models import Product, Comment, Like
from .forms import LoginForm, RegistrationForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Q


class HomeView(ListView):
    template_name = 'core/index.html'
    context_object_name = 'products'
    model = Product


class SearchResults(HomeView):
    def get_queryset(self):
        print(self.request.GET)
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(title__iregex=query) | Q(short_description__iregex=query)
        )


def get_products_by_category(request, category_id):
    products = Product.objects.filter(category__id=category_id)
    context = {
        'products': products
    }
    return render(request, 'core/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    comments = Comment.objects.filter(product=product)
    try:
        product.likes
    except Exception as e:
        Like.objects.create(product=product)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.product = product
            form.save()
            return redirect('products_detail', product.pk)
    else:
        form = CommentForm()
        total_likes = product.likes.user.all().count()

    context = {
        'product': product,
        'form': form,
        'comments': comments,
        'total_likes': total_likes
    }
    return render(request, 'core/detail.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'core/login.html', context)


def registration_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'core/registration.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def add_like(request, obj_id):
    from django.shortcuts import get_object_or_404
    obj = get_object_or_404(Product, pk=obj_id)
    try:
        obj.likes
    except Exception as e:
        Like.objects.create(product=obj)

    if request.user in obj.likes.user.all():
        obj.likes.user.remove(request.user.pk)
    else:
        obj.likes.user.add(request.user.pk)

    return redirect(request.environ['HTTP_REFERER'])


def liked_products(request):
    favorites = Like.objects.filter(user=request.user)
    products = [favorite.product for favorite in favorites]
    context = {
        'products': products
    }
    return render(request, 'core/author.html', context)


# def add_cart(request, object_id):
#     from django.shortcuts import get_object_or_404
#     obj = get_object_or_404(Product, pk=object_id)
#     try:
#         obj.carts
#     except Exception as e:
#         Cart.objects.create(product=obj)
#
#     if request.user in obj.carts.user.all():
#         obj.carts.user.remove(request.user.pk)
#     else:
#         obj.carts.user.add(request.user.pk)
#     return redirect(request.environ['HTTP_REFERER'])
#
#
def in_cart_products(request):
    return render(request, 'core/cart_author.html')


# def author_products(request, obj_id):
    # user = User.objects.get(username=username)
    # products = Like.objects.get(product_id=user)
    # context = {
    #     'products': products
    # }
    # return render(request, 'core/author.html', context)