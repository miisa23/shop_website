from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('categories/<int:category_id>', views.get_products_by_category, name='category_products'),
    path('products/<int:product_id>/', views.product_detail, name='products_detail'),
    path('search/', views.SearchResults.as_view(), name='search'),

    path('<int:obj_id>/', views.add_like, name='add_like'),
    path('author/', views.liked_products, name='liked_products'),

    # path('<int:object_id>/', views.add_cart, name='add_cart'),
    path('cart_author/', views.in_cart_products, name='in_cart_products')

]
