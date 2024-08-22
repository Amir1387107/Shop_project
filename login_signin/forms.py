from django import forms
from django.core.validators import RegexValidator
from .models import *


class SigninForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'repeat_password', 'email')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),
            'repeat_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        }

