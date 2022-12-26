from django.contrib import admin
from atexit import register
from .models import User
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(User)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'email', 'is_subscribe', 'is_free',)
    search_fields = ('username', 'email', 'is_subscribe', 'is_free',)