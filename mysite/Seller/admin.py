from django.contrib import admin
from .models import Cart, Product, Seller
# Register your models here.


admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Cart)