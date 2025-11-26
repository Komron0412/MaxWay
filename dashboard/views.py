from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic

from food_menu.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services

def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    categories = services.get_categories()
    products = services.get_products()
    users = services.get_users()
    orders = services.get_orders()
    ctx={
        'counts' : {
            'categories':len(categories),
            'images':len(products),
            'users':len(users),
            'orders':len(orders),
        }
    }
    return render(request, 'index.html', ctx)

#Category
@login_required_decorator
def category_create(request):
    model = Categories()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created category: {request.POST.get('name')}"]
        request.session["actions"] = actions

        category_count = request.session.get('category_count', 0)
        category_count += 1
        request.session["category_count"] = category_count

        return redirect('category_list')

    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'category/form.html',ctx)

@login_required_decorator
def category_edit(request,pk):
    model = Categories.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited category: {request.POST.get('name')}"]
        request.session["actions"] = actions

        return redirect('category_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'category/form.html',ctx)

@login_required_decorator
def category_delete(request,pk):
    model = Categories.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted category: {request.POST.get('name')}"]
    request.session["actions"] = actions

    return redirect('category_list')

@login_required_decorator
def category_list(request):
    categories=services.get_categories()
    print(categories)
    ctx={
        "categories":categories
    }
    return render(request,'category/list.html',ctx)

# Pruduct
@login_required_decorator
def product_create(request):
    model = Products()
    form = ProductForm(request.POST or None,request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You created product: {request.POST.get('name')}"]
        request.session["actions"] = actions

        product_count = request.session.get('product_count', 0)
        product_count +=1
        request.session["product_count"] = product_count

        return redirect('product_list')

    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'product/form.html',ctx)

@login_required_decorator
def product_edit(request,pk):
    model = Products.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited product: {request.POST.get('name')}"]
        request.session["actions"] = actions

        return redirect('product_list')

    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'product/form.html',ctx)

@login_required_decorator
def product_delete(request,pk):
    model = Products.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted product: {request.POST.get('name')}"]
    request.session["actions"] = actions

    return redirect('product_list')

@login_required_decorator
def product_list(request):

    products=services.get_products()

    ctx={
        "products":products
    }
    return render(request,'product/list.html',ctx)

#User
@login_required_decorator
def user_create(request):
    model = Users()
    form = UserForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created user: {request.POST.get('name')}"]
        request.session["actions"] = actions

        user_count = request.session.get('user_count', 0)
        user_count += 1
        request.session["user_count"] = user_count

        return redirect('user_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'user/form.html',ctx)

@login_required_decorator
def user_edit(request,pk):
    model = Users.objects.get(pk=pk)
    form = UserForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited user: {request.POST.get('name')}"]
        request.session["actions"] = actions

        return redirect('user_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'user/form.html',ctx)

@login_required_decorator
def user_delete(request,pk):
    model = Users.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted user: {request.POST.get('name')}"]
    request.session["actions"] = actions

    return redirect('user_list')

@login_required_decorator
def user_list(request):
    users=services.get_users()
    ctx={
        "users":users
    }
    return render(request,'user/list.html',ctx)

#orders
@login_required_decorator
def order_list(request):
    orders=services.get_orders()
    ctx={
        "orders":orders
    }
    return render(request,'order/list.html',ctx)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "signup.html"

@login_required_decorator
def profile(request):
    return render(request,'profile.html')