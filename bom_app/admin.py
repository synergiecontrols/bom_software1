from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('head', 'make', 'mat_name', 'type_no', 'least_price', 'discount')
    search_fields = ('head','make', 'mat_name', 'type_no')