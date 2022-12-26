from django.contrib import admin
from atexit import register
from .models import QRrecord, QRCategory
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(QRrecord)
class QRrecordAdmin(ModelAdmin):
    list_display = ('name', 'is_active', 'qr_category',)
    search_fields = ('name', 'user_id', 'qr_category', 'is_active',)


@register(QRCategory)
class QRCategoyAdmin(ModelAdmin):
    list_display = ('name', 'user_id',)
    search_fields = ('name', 'user_id',)