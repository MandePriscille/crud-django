from django.contrib import admin

# Register your models here.

from .models import Product, Achat, User

admin.site.register(Product)
admin.site.register(Achat)
