from django.contrib import admin
from . import models

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_filter = ['is_read_by_admin']
    


admin.site.register(models.ContactUs,ContactAdmin)