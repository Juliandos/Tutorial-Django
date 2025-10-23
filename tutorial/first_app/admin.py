from django.contrib import admin
from .models import Category, MenuItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'menu_items_count', 'created_at']
    search_fields = ['name', 'description']
    list_per_page = 20
    
    def menu_items_count(self, obj):
        return obj.menu_items.count()
    menu_items_count.short_description = 'Nº de Platos'


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'is_vegetarian', 'spicy_level', 'preparation_time']
    list_filter = ['category', 'is_available', 'is_vegetarian', 'spicy_level']
    search_fields = ['name', 'description']
    list_editable = ['price', 'is_available']
    list_per_page = 20
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'category', 'description')
        }),
        ('Precio y Disponibilidad', {
            'fields': ('price