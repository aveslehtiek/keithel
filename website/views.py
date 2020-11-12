from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, ServiceArea, ExchangeMethod, PaymentMethod, Profile
from .forms import ProductForm, UpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    users = User.objects.all()
    products = Product.objects.all()
    # service_area_query = Profile.objects.values('user', 'service_area')
    # service_area_list = list(service_area_query)
    # exchange_method_query = Profile.objects.values('user', 'exchange_method')
    # exchange_method_list = list(exchange_method_query)
    # payment_method_query = Profile.objects.values('user', 'payment_method')
    # payment_method_list = list(payment_method_query)
    return render(request, 'home.html', {'users':users, 'products':products})   # 'service_area':service_area_list, 'exchange_method':exchange_method_list, 'payment_method':payment_method_list

# class HomeView(ListView):
#     model = Product
#     template_name = 'home.html'
#     # ordering = ['-id']

def CategoryView(request, category):
    category_products = Product.objects.filter(category=category.replace('-', ' '))
    return render(request, 'categories.html', {'category':category.title().replace('-', ' '), 'category_products':category_products})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'

class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    # fields = '__all__'

class UpdateProductView(UpdateView):
    model = Product
    form_class = UpdateForm
    template_name = 'update_product.html'
    # fields = ['name', 'description']

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('home')
