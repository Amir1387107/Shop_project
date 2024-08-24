from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import SigninForm
from .models import UserOfSite
# Create your views here.


class loginView(View):
    def get(self, request):
        context = {'SigninForm': SigninForm}
        return render(request, 'login_signin/login_page.html', context)

    def post(self, request):
        Form = SigninForm(request.POST)
        if Form.is_valid():
            user = UserOfSite(username=Form.cleaned_data['username'], email=Form.cleaned_data['email']
            ,password=Form.cleaned_data['password'], phone_number=Form.cleaned_data['phone_number'])
            user.save()
            return redirect(reverse('home_page'))
        error=None
        if UserOfSite.objects.filter(username=Form.cleaned_data['username']).exists():
            error = 'نام کاربری در سایت موجود می باشد'
        elif UserOfSite.objects.filter(email=Form.cleaned_data['email']).exists():
            error = 'ایمیل مورد نظر در سایت ثبت نام کرده است'
        elif UserOfSite.objects.filter(phone_number=Form.cleaned_data['phone_number']).exists():
            error = 'شماره تلفن مورد نظر در سایت ثبت شده است'
        context = {'SigninForm': SigninForm, 'error': error}
        return render(request, 'login_signin/login_page.html', context)
