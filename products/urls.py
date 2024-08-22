from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home_page'),
    path('buy/<int:int>', views.OrdersView.as_view(), name='Order_page'),
]