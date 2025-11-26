from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100,null=False, blank=False)
    category = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='images', null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False,unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    payment_type = models.SmallIntegerField(null=False, blank=False)
    status = models.SmallIntegerField(null=False, blank=False,default=1)
    address = models.CharField(max_length=100, null=False, blank=False)
    customer = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    created = models.DateField(auto_now_add=True)

