from django.contrib import admin
from .models import *


# Register your models here.

class design(admin.ModelAdmin):
    list_display_links = ['model',]
    list_filter = ['kind','color']
    list_display = ['model', 'color', "price"]
    # readonly_fields = ["slug"]
    # prepopulated_fields = {'slug':['id','kind','model','color']}
    list_editable  = []
    search_fields = ['model','color','details']




class debtsdesign(admin.ModelAdmin):
    list_filter = ['creditor','amount_of_debt','payment_deadline']


class requestsdesign(admin.ModelAdmin):
    list_filter = ['debtor','amount_of_debt','payment_deadline']


class Ordersdesign(admin.ModelAdmin):
    list_display = ['Buyer', 'product_model', 'product_color']
    list_display_links = ['Buyer']
    list_filter = ['is_read']


admin.site.register(Products, design)
admin.site.register(Kind)
admin.site.register(Orders, Ordersdesign)
admin.site.register(Debts, debtsdesign)
admin.site.register(Requests, requestsdesign)

