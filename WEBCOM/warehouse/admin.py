from django.contrib import admin
from .models import Item,Customer
# Register your models here.


class AdminItem(admin.ModelAdmin):
	list_display = ['name', 'price', 'desc']
	

admin.site.register(Item, AdminItem)
admin.site.register(Customer)