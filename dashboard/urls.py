from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),

    path('category/create/', category_create, name='category_create'),
    path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
    path('category/list/', category_list, name='category_list'),

    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
    path('product/list/', product_list, name='product_list'),

    path('user/create/', user_create, name='user_create'),
    path('user/<int:pk>/edit/', user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', user_delete, name='user_delete'),
    path('user/list/', user_list, name='user_list'),

    path('order/list/', order_list, name='order_list'),

    path('profile/',profile, name='profile'),

    path('signup/', SignUpView.as_view(), name='signup'),
]