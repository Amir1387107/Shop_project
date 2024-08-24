from login_signin import views
from django.urls import path

urlpatterns = [
    path('', views.loginView.as_view(), name='login'),
]