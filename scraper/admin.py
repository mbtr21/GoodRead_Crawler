from django.contrib import admin
from django.contrib.admin import register
from .models import Book, Group
# Register your models here.


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_info')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'title', 'publication_info')
    search_fields = ('title', 'genres')


@register(Group)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('title', 'location')
