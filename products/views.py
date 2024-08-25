from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Products, UserOfSite
from .models import Kind, Orders
from .forms import OrdersModelForm, SigninForm, LoginForm

Product=Products


class loginView(View):
    def get(self, request):
        context = {'SigninForm': SigninForm, 'loginForm': LoginForm}
        return render(request, 'products/login_page.html', context)

    def post(self, request):
        Post=request.POST
        Form = SigninForm(Post)
        if Form.is_valid():
            error = None
            if UserOfSite.objects.filter(username=Form.cleaned_data['username']).exists():
                error = 'نام کاربری در سایت موجود می باشد'
            elif UserOfSite.objects.filter(email=Form.cleaned_data['email']).exists():
                error = 'ایمیل مورد نظر در سایت ثبت نام کرده است'
            elif UserOfSite.objects.filter(phone_number=Form.cleaned_data['phone_number']).exists():
                error = 'شماره تلفن مورد نظر در سایت ثبت شده است'
            if error is not None:
                context = {'SigninForm': SigninForm, 'loginForm': LoginForm, 'error': error}
                return render(request, 'products/login_page.html', context)
            if Form.is_valid():
                user = UserOfSite(username=Form.cleaned_data['username'], email=Form.cleaned_data['email']
                ,password=Form.cleaned_data['password'], phone_number=Form.cleaned_data['phone_number'])
                user.save()
                User = UserOfSite.objects.get(username=Form.cleaned_data['username'], password=Form.cleaned_data['password'])
                return render(request, 'products/index_page.html', context={
                    'User': User,
                    'Mobleman': Product.objects.filter(kind=1).values(),
                    'Komod': Product.objects.filter(kind=4).values(),
                    'Edari': Product.objects.filter(kind=3).values(),
                    'Miz_Arayesh': Product.objects.filter(kind=6).values(),
                    'Dravel': Product.objects.filter(kind=8).values(),
                    'Jakafshi': Product.objects.filter(kind=9).values(),
                    'Dekor': Product.objects.filter(kind=10).values(),
                    'Miz_Nahar_Khory': Product.objects.filter(kind=11).values(),
                    'KalayeKhab': Product.objects.filter(kind=12).values(),
                    'MasnoateFelezi': Product.objects.filter(kind=13).values(),
                })

        Form_sing = LoginForm(Post)
        if Form_sing.is_valid():
            if UserOfSite.objects.filter(username=Form_sing.cleaned_data['username'], password=Form_sing.cleaned_data['password']).exists():
                User = UserOfSite.objects.get(username=Form_sing.cleaned_data['username'], password=Form_sing.cleaned_data['password'])
                return render(request, 'products/index_page.html', context={
                    'User': User,
                    'Mobleman': Product.objects.filter(kind=1).values(),
                    'Komod': Product.objects.filter(kind=4).values(),
                    'Edari': Product.objects.filter(kind=3).values(),
                    'Miz_Arayesh': Product.objects.filter(kind=6).values(),
                    'Dravel': Product.objects.filter(kind=8).values(),
                    'Jakafshi': Product.objects.filter(kind=9).values(),
                    'Dekor': Product.objects.filter(kind=10).values(),
                    'Miz_Nahar_Khory': Product.objects.filter(kind=11).values(),
                    'KalayeKhab': Product.objects.filter(kind=12).values(),
                    'MasnoateFelezi': Product.objects.filter(kind=13).values(),
                })

        error = None
        if UserOfSite.objects.filter(username=Form_sing.cleaned_data['username']).exists():
            error = 'رمز عبور صحیح نمی باشد'
        elif UserOfSite.objects.filter(phone_number=Form_sing.cleaned_data['password']).exists():
            error = 'نام کاربری صحیح نمی باشد'
        if error is not None:
            context = {'SigninForm': SigninForm, 'loginForm': LoginForm, 'error_log': error}
            return render(request, 'products/login_page.html', context)


class OrdersView(View):
    def get(self, request, int):
        OrderForm = OrdersModelForm()
        id_found = Products.objects.all().get(id=int)

        return render(request, 'products/product_buying.html', {
            'OrdersForm': OrderForm,
            'product': id_found
        })

    def post(self, request, int):
        OrderForm = OrdersModelForm(request.POST)
        id_found = Products.objects.all().get(id=int)

        if OrderForm.is_valid():
            OrderForm.cleaned_data['product_model'] = id_found.model
            OrderForm.cleaned_data['product_color'] = id_found.color
            Model = Orders(product_model=OrderForm.cleaned_data['product_model'], Buyer=OrderForm.cleaned_data['Buyer'],
                           Phone_one=OrderForm.cleaned_data['Phone_one'],
                           Phone_two=OrderForm.cleaned_data['Phone_two'],
                           email=OrderForm.cleaned_data['email'],
                           Address=OrderForm.cleaned_data['Address'],
                           product_color=OrderForm.cleaned_data['product_color'])
            Model.save()
            return redirect('home_page')
        return render(request, 'products/product_buying.html', {
            'OrdersForm': OrderForm,
            'product': id_found  
        })
    

def site_header_component(request):
    return render(request, 'shared/site_header_component.html')


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')


