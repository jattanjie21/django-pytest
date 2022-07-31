from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')
    list_display_links = ('name',)
    search_fields = ('name', 'phone', 'email', 'address')
    list_filter = ('name', 'phone', 'email', 'address')
    ordering = ('name',)
    fields = ('name', 'phone', 'email', 'address')