from django.shortcuts import render
from products.models import UserOfSite
from cart.models import Product


# Create your views here.


def index(request, username, password):
    try:
        data = Product.objects.all().filter(user=username)
    except:
        data = []
    context = {'data': data, 'User':UserOfSite.objects.get(username=username, password=password)}
    return render(request, 'cart/cartpage.html', context=context)

