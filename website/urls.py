from django.urls import path
from . import views
from .views import ProductDetailView, AddProductView, UpdateProductView, DeleteProductView, CategoryView # HomeView,

urlpatterns = [
    path('', views.home, name='home'),
    # path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('product/edit/<int:pk>', UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/delete', DeleteProductView.as_view(), name='delete_product'),
    path('category/<str:category>/', CategoryView, name='category'),
]
