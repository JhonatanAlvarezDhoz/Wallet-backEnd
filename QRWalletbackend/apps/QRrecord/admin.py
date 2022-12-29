from django.contrib import admin
from atexit import register
from .models import QRrecord, QRCategory
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(QRrecord)
class QRrecordAdmin(ModelAdmin):

    list_display = ('name', 'is_active', 'get_user', 'qr_category',)
    search_fields = ('name', 'user_id', 'qr_category', 'is_active',)

    @admin.display(ordering='qr_category__user_id', description='username')
    def get_user(self, obj):
        return obj.qr_category.user_id


@register(QRCategory)
class QRCategoyAdmin(ModelAdmin):
    list_display = ('name', 'user_id',)
    search_fields = ('name', 'user_id',)