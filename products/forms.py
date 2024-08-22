from django import forms
from django.core.validators import RegexValidator
from .models import Orders, Products


class OrdersForm(forms.Form):
    product_model = forms.CharField(label='اسم محصول', initial='')
    product_color = forms.CharField(label='رنگ محصول', initial='')
    Buyer = forms.CharField(label='نام و نام خانوادگی خریدار')
    Phone_one = forms.IntegerField(label='شماره همراه اول', validators=[RegexValidator(r'^\d{11}$')])
    Phone_two = forms.IntegerField(label='شماره همراه دوم', validators=[RegexValidator(r'^\d{11}$')])
    email = forms.EmailField(label='ایمیل')
    Address = forms.CharField(label='آدرس')
    
class OrdersModelForm(forms.ModelForm):
    product_model = forms.CharField(required=False)
    product_color = forms.CharField(required=False)
    class Meta:
        model = Orders

        fields = ['product_model', 'product_color', 'Buyer', 'Phone_one', 'Phone_two', 'email', 'Address']

        widgets = {
            'product_model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام محصول'}),
            'product_color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رنگ محصول'}),
            'Buyer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'Phone_one':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ' شماره تلفن همراه اول' }),
            'Phone_two':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن همراه دوم' }),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس'}),
        }



