from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.first_name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):        
        return self.name

class Achat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_achat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name