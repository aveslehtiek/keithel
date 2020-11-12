from django import forms
from .models import Product,  Category

# category_choices = Category.objects.all().values_list('category_name', 'category_name')

# category_choice_list = []
# for item in category_choices:
#     category_choice_list.append(item)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'seller', 'description', "header_image")  # 'category',

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'seller': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'seller', 'type': 'hidden'}),
            # 'seller': forms.Select(attrs={'class': 'form-control'}),
            # 'category': forms.Select(choices=category_choice_list, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'seller': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }