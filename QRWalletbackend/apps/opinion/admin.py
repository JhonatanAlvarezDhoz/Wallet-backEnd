from django.contrib import admin
from atexit import register
from .models import Opinion, Category
from django.contrib.admin import ModelAdmin, register
# Register your models here.

@register(Category)
class OpinionCategoryAdmin(ModelAdmin):
    list_display = ('id', 'name_category',)


@register(Opinion)
class OpinionAdmin(ModelAdmin):
    list_display = ('title', 'opinion_category', 'user', 'is_active',)
    search_fields = ('title', 'opinion_category', 'user', 'is_active',)


