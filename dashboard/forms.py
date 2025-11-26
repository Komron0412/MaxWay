from django import forms
from food_menu.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields= "__all__"
        widgets = {
        "title":forms.TextInput(attrs={'class':'form-control'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields= "__all__"
        widgets = {
        "name":forms.TextInput(attrs={'class':'form-control'})
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields= "__all__"
        widgets = {
        "name":forms.TextInput(attrs={'class':'form-control'})
        }

