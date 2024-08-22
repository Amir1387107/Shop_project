from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import BuyForm, SellForm
from .models import SellModel
from products.models import Products as Prod
from products.models import Requests


class SellView(View):
    def get(self, request):
        buying = SellForm()
        return render(request, 'Factor/Factor_Sell.html', {
            'SellForm': buying,
        })

    def post(self, request):
        buying = SellForm(request.POST)
        if buying.is_valid():
            buying.cleaned_data['price'] = Prod.objects.all().filter(model=buying.cleaned_data['model'], color=buying.cleaned_data['color'])[0].price
            model = buying.cleaned_data['model']
            color = buying.cleaned_data['color']
            price = buying.cleaned_data['price']
            buyer = buying.cleaned_data['buyer']
            number = buying.cleaned_data['number']


            Model = SellModel(model=model, color=color, buyer=buyer, price=price, number=number)
            Model.save()

            return render(request, 'Factor/accepted_sell.html')
        return render(request, 'Factor/Factor_Sell.html', {
            'SellForm': buying,
        })

# Create your views here.


class BuyView(View):
    def get(self, request):
        buying = BuyForm()
        return render(request, 'Factor/Factor_Buy.html', {
            'BuyForm': buying,


        })

    def post(self, request):
        buying = BuyForm(request.POST)
        if buying.is_valid():
            number = buying.cleaned_data['number']
            buying.cleaned_data['number'] = None
            for i in range(number):
                buying = BuyForm(request.POST)
                if buying.is_valid():
                    buying.save()
            return render(request, 'Factor/accepted_buy.html')
        return render(request, 'Factor/Factor_Buy.html', {
            'BuyForm': buying,


        })


def SellFactor(request):
    products = SellModel.objects.all()
    buyer = ''
    sum = 0
    amount_debt = 0
    for product in products:
        buyer = product.buyer
        try:
            for i in range(product['number']):
                sum+=int(product.price)
        except:
            for i in range(product.number):
                sum+=int(product.price)


    try:
        amount_debt = Requests.objects.all().get(debtor=buyer).amount_of_debt
    except:
        pass
    context = {'product_data': products, 'buyer': buyer, 'debt': amount_debt, 'sum':sum}
    return render(request, 'Factor/Sell_Factor.html', context)

def EmptySellModel(request):
    all = SellModel.objects.all()
    for product in all:
        for number in range(product.number):
            Prod.objects.all().filter(model=product.model).delete()
    SellModel.objects.all().delete()
    return render(request,'Factor/Empty.html')