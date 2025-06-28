from django.contrib import admin
from .models import MyUser
# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    """Класс админ"""
    list_display = (
        'username',
        'email',
        'date_birth'
    )
    search_fields = ('username',)