from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginView.as_view(), name='login'),
    path('buy/<int:int>', views.OrdersView.as_view(), name='Order_page'),
    path('details/<int:pk>/<str:Username>/<str:password>', views.product_details.as_view(), name='details'),
    path('buy/<int:pk>/<str:Username>/<str:password>', views.buy, name='buy'),
]
