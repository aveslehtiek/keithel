from django.contrib import admin
from .models import Product, Category, Profile, ServiceArea, ExchangeMethod, PaymentMethod

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(ServiceArea)
admin.site.register(ExchangeMethod)
admin.site.register(PaymentMethod)
