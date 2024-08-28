from django import forms
from django.core.validators import RegexValidator
from products.models import *
from .models import *


class BuyForm(forms.ModelForm):
    kind = forms.ModelMultipleChoiceField(label='دسته', widget=forms.CheckboxSelectMultiple, queryset=Kind.objects.all(), required=True)
    number = forms.IntegerField(widget=forms.NumberInput, label='تعداد', initial=1)
    class Meta:
        model = Products

        fields = ['model', 'price', 'color', 'details', 'kind', 'image1', 'image2', 'image3', 'image4']

        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'مدل محصول'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'قیمت'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رنگ'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات تکمیلی'}),
            'kind': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'placeholder': 'دسته'}),
            'number' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تعداد'})
        }


class SellForm(forms.ModelForm):
    model = forms.CharField(widget=forms.TextInput(), label='مدل محصول')
    color = forms.CharField(widget=forms.TextInput(), label='رنگ')
    number = forms.IntegerField(widget=forms.NumberInput(), label='تعداد')

    class Meta:
        model = SellModel

        fields = ['number', 'model', 'color', 'price']


class MoreForm(forms.ModelForm):
    class Meta:
        model = More

        fields = '__all__'

        widgets = {
            'buyer':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'خریدار'}),
            'details':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'توضیحات'}),
            'off':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تخفیف به ریال'})
        }