from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/<str:password>', views.index, name='cart_page'),
]