from django import forms
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator
from .models import UserOfSite


class SigninForm(forms.Form):
    username = forms.CharField(label='Username', max_length=3000,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),

                               error_messages={'unique':'این نام کاربری قبلا وارد شده است'})
    password = forms.CharField(label='Password', max_length=20, validators=[MinLengthValidator(8), MaxLengthValidator(20)],
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
    phone_number = forms.CharField(label='Phone Number', max_length=11, validators=[RegexValidator(r'^\d{11}$')],
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تلفن همراه'}),

                                   error_messages={'unique':'این شماره تلفن قبلا وارد شده است'})
    email = forms.EmailField(label='Email', max_length=3000
                             ,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),

                             error_messages={'unique':'این ایمیل قبلا وارد شده است'})

# class SigninForm(forms.ModelForm):
#
#     class Meta:
#         model = UserOfSite
#         fields = ('username', 'password', 'email', 'phone_number')
#
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),
#             'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تلفن همراه'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
#         }
#
#         error_messages = {
#             'username':{'unique':'این نام کاربری قبلا وارد شده است'},
#             'phone_number': {'unique': 'این شماره تلفن قبلا وارد شده است'},
#             'email': {'unique': 'این ایمیل قبلا وارد شده است'},
#         }

