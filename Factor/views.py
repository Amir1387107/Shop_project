from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .forms import BuyForm, SellForm, MoreForm
from .models import SellModel, More, SellModelSave, Factors
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
            buying.cleaned_data['price'] = \
            Prod.objects.all().filter(model=buying.cleaned_data['model'], color=buying.cleaned_data['color'])[0].price
            model = buying.cleaned_data['model']
            color = buying.cleaned_data['color']
            price = buying.cleaned_data['price']
            number = buying.cleaned_data['number']
            if Prod.objects.all().filter(model=model, color=color).exists():
                pass
            else:
                return HttpResponse('محصول موجود نمی باشد')

            Model = SellModel(model=model, color=color, price=price, number=number)
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


class MoreView(View):
    def get(self, request):
        More = MoreForm()
        return render(request, 'Factor/More.html', {'More': More})

    def post(self, request):
        More = MoreForm(request.POST)
        if More.is_valid():
            More.save()
            return render(request, 'Factor/accepted_sell2.html')
        return render(request, 'Factor/More.html', {'More': More})


def SellFactor(request):
    products = SellModel.objects.all()
    buyer = ''
    sum = 0
    amount_debt = 0
    detail = None
    date = None
    off = 0
    if More.objects.all():
        detail = More.objects.all()[0].details
        off = More.objects.all()[0].off
        buyer = More.objects.all()[0].buyer
        date = More.objects.all()[0].date

    for product in products:
        sum += product.price * product.number
    try:
        amount_debt = Requests.objects.all().get(debtor=buyer).amount_of_debt
    except:
        pass

    try:
        x = int(Factors.objects.all().last().id)+1
    except:
        x = 1

    sum_all = sum - off
    context = {'pk': x, 'product_data': products, 'date': date, 'buyer': buyer, 'debt': amount_debt, 'sum': sum, 'off': off,
               'sum_all': sum_all, 'details': detail}
    return render(request, 'Factor/Sell_Factor.html', context)


def SellFactorSaved(request, pk):
    model = Factors.objects.all().get(id=pk)

    buyer = model.buyer
    sum = 0
    amount_debt = 0
    detail = model.details
    date = model.date
    off = model.off
    products = model.productsadded.all()

    for product in products:
        sum += product.price * product.number
    try:
        amount_debt = Requests.objects.all().get(debtor=buyer).amount_of_debt
    except:
        pass

    sum_all = sum - off
    context = {'pk': pk, 'product_data': products, 'date': date, 'buyer': buyer, 'debt': amount_debt, 'sum': sum, 'off': off,
               'sum_all': sum_all, 'details': detail}
    return render(request, 'Factor/Sell_Factor.html', context)


def EmptySellModel(request):
    all = SellModel.objects.all()
    more=More.objects.all()[0]
    for product in all:
        for number in range(product.number):
            Prod.objects.all().filter(model=product.model).delete()
    fact = Factors(date=more.date, buyer=more.buyer, off=more.off, details=more.details)
    fact.save()
    for product in all:
        num = product.number
        price = product.price
        color = product.color
        model = product.model
        Save = SellModelSave(number=num, price=price, color=color, model=model)
        Save.save()
        fact.productsadded.add(Save)

    SellModel.objects.all().delete()
    More.objects.all().delete()
    return render(request, 'Factor/Empty.html')
