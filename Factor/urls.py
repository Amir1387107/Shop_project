from Factor import views
from django.urls import path

urlpatterns = [
    path('buy/', views.BuyView.as_view(), name='buy'),
    path('sell/', views.SellView.as_view(), name='sell'),
    path('sell/factor', views.SellFactor, name='sellFactor'),
    path('Empty', views.EmptySellModel, name="EmptySellModel" ),
]
