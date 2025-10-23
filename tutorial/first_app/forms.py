from django import forms
from .models import Category, MenuItem

class CategoryForm(forms.ModelForm):
    """Formulario para crear y editar categorías"""
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Entradas, Platos fuertes, Postres...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción opcional de la categoría'
            }),
        }
        labels = {
            'name': 'Nombre de la categoría',
            'description': 'Descripción',
        }


class MenuItemForm(forms.ModelForm):
    """Formulario para crear y editar platos del menú"""
    class Meta:
        model = MenuItem
        fields = [
            'name', 'category', 'description', 'price',
            'is_available', 'is_vegetarian', 'spicy_level',
            'preparation_time'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Bandeja Paisa'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe el plato, sus ingredientes y preparación'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'is_vegetarian': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'spicy_level': forms.Select(attrs={
                'class': 'form-control'
            }),
            'preparation_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Minutos'
            }),
        }
        labels = {
            'name': 'Nombre del plato',
            'category': 'Categoría',
            'description': 'Descripción',
            'price': 'Precio (COP)',
            'is_available': '¿Está disponible?',
            'is_vegetarian': '¿Es vegetariano?',
            'spicy_level': 'Nivel de picante',
            'preparation_time': 'Tiempo de preparación (minutos)',
        }