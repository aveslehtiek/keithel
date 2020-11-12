from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('home')

class ServiceArea(models.Model):
    service_area =models.CharField(max_length=255)

    def __str__(self):
        return self.service_area

    def get_absolute_url(self):
        return reverse('home')

class ExchangeMethod(models.Model):
    exchange_method = models.CharField(max_length=255)

    def __str__(self):
        return self.exchange_method

    def get_absolute_url(self):
        return reverse('home')

class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        return self.payment_method

    def get_absolute_url(self):
        return reverse('home')


# service_area = ServiceArea.objects.all().values_list('service_area', 'service_area')

# service_area_list = []
# for item in service_area:
#     service_area_list.append(item)
# service_area_tuple = tuple(service_area_list)

# exchange_method = ExchangeMethod.objects.all().values_list('exchange_method', 'exchange_method')

# exchange_method_list = []
# for item in exchange_method:
#     exchange_method_list.append(item)
# exchange_method_tuple = tuple(exchange_method_list)

# payment_method = PaymentMethod.objects.all().values_list('payment_method', 'payment_method')

# payment_method_list = []
# for item in payment_method:
#     payment_method_list.append(item)
# payment_method_tuple = tuple(payment_method_list)


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    # service_area = MultiSelectField(null=True, blank=True, choices=service_area_tuple)
    # payment_method = MultiSelectField(null=True, blank=True, choices=payment_method_tuple)
    # exchange_method = MultiSelectField(null=True, blank=True, choices=exchange_method_tuple)
    website_url = models.CharField(null=True, blank=True, max_length=255)
    facebook_url = models.CharField(null=True, blank=True, max_length=255)
    instagram_url = models.CharField(null=True, blank=True, max_length=255)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Product(models.Model):
    name = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to="images/", default="images/sample.png")
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    # category = models.CharField(null=True, blank=True, max_length=255)
    service_area = models.CharField(null=True, blank=True, max_length=255)
    payment_method = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.name + ' | ' + str(self.seller)

    def get_absolute_url(self):
        return reverse('product-detail', args=(str(self.id)))