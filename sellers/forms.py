from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from website.models import Profile, ServiceArea, ExchangeMethod, PaymentMethod


service_area = ServiceArea.objects.all().values_list('service_area', 'service_area')

service_area_list = []
for item in service_area:
    service_area_list.append(item)
service_area_tuple = tuple(service_area_list)

exchange_method = ExchangeMethod.objects.all().values_list('exchange_method', 'exchange_method')

exchange_method_list = []
for item in exchange_method:
    exchange_method_list.append(item)
exchange_method_tuple = tuple(exchange_method_list)

payment_method = PaymentMethod.objects.all().values_list('payment_method', 'payment_method')

payment_method_list = []
for item in payment_method:
    payment_method_list.append(item)
payment_method_tuple = tuple(payment_method_list)

class ProfilePageForm(forms.ModelForm):
    

    class Meta:
        model = Profile
        fields = ('service_area', 'payment_method', 'exchange_method', 'website_url', 'facebook_url', 'instagram_url')
        

        widgets = {
            'service_area': forms.CheckboxSelectMultiple(choices=service_area_tuple),
            'payment_method': forms.CheckboxSelectMultiple(choices=payment_method_tuple),
            'exchange_method': forms.CheckboxSelectMultiple(choices=exchange_method_tuple),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        #  'first_name', 'last_name', 'email',

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    #  'first_name', 'last_name', 'email', , 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined'

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
