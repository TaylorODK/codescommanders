from django.contrib import admin
from .models import Order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Класс для включения в админку модели Order"""
    list_display = (
        'name',
        'description',
        'user'
    )
    search_fields = ('user',)
