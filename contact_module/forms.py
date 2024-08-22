from django import forms
from django.core.validators import RegexValidator
from contact_module.models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی', max_length=50,
                                error_messages={
                                    'required': 'لطفا نام و نام خوانوادگی خود را وارد کنید',
                                    'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'
                                },
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'نام و نام خانوادگی'
                                }))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ایمیل'
    }))
    phone_number = forms.IntegerField(validators=[RegexValidator(r'^\d{11}$')])
    subject = forms.CharField(label='موضوع', max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'عنوان'}))
    message = forms.CharField(label='پیام',widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'متن پیام', 'id':'message'}))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
        # fields = '__all__'

        # exclude = ['email'] #this says everything but email

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'phone_number':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن همراه' }),
            'subject' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}),
            'message' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام', 'id': 'message'})
        }

        labels = {
            'full_name':'نام و نام خانوادگی',
            'phone_number':'شماره تلفن همراه'
        }
        error_messages = {
            'full_name': {'required': 'لطفا نام و نام خوانوادگی خود را وارد کنید','max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد' }
        }



