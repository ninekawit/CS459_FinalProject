from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'expire', 'image')
    list_display = ('name', 'description', 'price', 'expire', 'image')
    list_filter = ('name', 'expire')
    
admin.site.register(Item, ItemAdmin)