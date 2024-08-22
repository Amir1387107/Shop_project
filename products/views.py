from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Products
from .models import Kind, Orders
from .forms import OrdersModelForm

Product=Products


def HomePageView(request):
    Products=Product.objects.all().order_by('-price')
    return render(request, 'products/index_page.html', context={
        'products':Products,
        'Mobleman':Product.objects.filter(kind=1).values(),
        'Komod':Product.objects.filter(kind=4).values(),
        'Edari':Product.objects.filter(kind=3).values(),
        'Miz_Arayesh':Product.objects.filter(kind=6).values(),
        'Dravel':Product.objects.filter(kind=8).values(),
        'Jakafshi':Product.objects.filter(kind=9).values(),
        'Dekor':Product.objects.filter(kind=10).values(),
        'Miz_Nahar_Khory':Product.objects.filter(kind=11).values(),
        'KalayeKhab':Product.objects.filter(kind=12).values(),
        'MasnoateFelezi':Product.objects.filter(kind=13).values(),
    })


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


