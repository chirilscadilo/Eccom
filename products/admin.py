from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ProductCard)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShoeSize)
admin.site.register(ClothSize)
admin.site.register(ShippingAddress)