from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(primary_key=True, null=False, max_length=15)
    balance = models.IntegerField(default=0)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class Book(models.Model):
    author = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    pubdate = models.DateField()
    cost = models.BigIntegerField()
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class BookItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return "Item %s" % self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    shipping_cost = models.BigIntegerField(default=1000)

    def __str__(self):
        return "order %s" % self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return "Order Item %s" % self.order.id
