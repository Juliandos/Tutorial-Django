from django import forms
from django.core.exceptions import ValidationError
from .models import Menu, MenuCategory

# Opciones para campos de selección
RATING_CHOICES = [
    (1, '⭐ 1 Estrella'),
    (2, '⭐⭐ 2 Estrellas'),
    (3, '⭐⭐⭐ 3 Estrellas'),
    (4, '⭐⭐⭐⭐ 4 Estrellas'),
    (5, '⭐⭐⭐⭐⭐ 5 Estrellas'),
]

COUNTRY_CHOICES = [
    ('CO', 'Colombia'),
    ('MX', 'México'),
    ('AR', 'Argentina'),
    ('ES', 'España'),
    ('US', 'Estados Unidos'),
]

class RestaurantRegistrationForm(forms.Form):
    # Campo de texto simple
    restaurant_name = forms.CharField(
        max_length=100,
        label='Nombre del Restaurante',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: La Casa del Sabor'
        })
    )
    
    # Campo de email con validación automática
    email = forms.EmailField(
        label='Email de contacto',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@restaurante.com'
        })
    )
    
    # Campo de número entero
    year_established = forms.IntegerField(
        label='Año de fundación',
        min_value=1900,
        max_value=2025,
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )
    
    # Campo decimal
    average_price = forms.DecimalField(
        label='Precio promedio por persona',
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01'
        })
    )
    
    # Campo de selección (dropdown)
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        label='Calificación',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    # Campo de selección múltiple
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        label='País',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    # Campo de texto largo (textarea)
    description = forms.CharField(
        label='Descripción del restaurante',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Describe tu restaurante, su ambiente, especialidades...'
        }),
        required=False
    )
    
    # Campo de checkbox
    has_delivery = forms.BooleanField(
        label='¿Ofrece servicio a domicilio?',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    
    # Campo de checkboxes múltiples
    services = forms.MultipleChoiceField(
        choices=[
            ('wifi', 'WiFi Gratis'),
            ('parking', 'Estacionamiento'),
            ('terrace', 'Terraza'),
            ('live_music', 'Música en vivo'),
            ('kids_area', 'Área infantil'),
        ],
        label='Servicios disponibles',
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
    
    # Campo de radio buttons
    reservation_required = forms.ChoiceField(
        choices=[
            ('yes', 'Sí, siempre'),
            ('no', 'No es necesario'),
            ('weekends', 'Solo fines de semana'),
        ],
        label='¿Se requiere reservación?',
        widget=forms.RadioSelect(),
        initial='no'
    )
    
    # Campo de fecha
    opening_date = forms.DateField(
        label='Fecha de apertura',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    # Campo de hora
    opening_time = forms.TimeField(
        label='Hora de apertura',
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        })
    )
    
    # Campo de archivo/imagen
    logo = forms.ImageField(
        label='Logo del restaurante',
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        })
    )
    
    # Campo de URL
    website = forms.URLField(
        label='Sitio web',
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'https://ejemplo.com'
        })
    )
    
    # Campo de selección basado en modelo (ForeignKey)
    menu_category = forms.ModelChoiceField(
        queryset=MenuCategory.objects.all(),
        label='Categoría principal del menú',
        empty_label='Selecciona una categoría',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    # Campo de contraseña
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    
    # Campo de confirmación de contraseña
    password_confirm = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    
    # Validación personalizada a nivel de formulario
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Las contraseñas no coinciden')
        
        return cleaned_data
    
    # Validación personalizada de un campo específico
    def clean_restaurant_name(self):
        name = self.cleaned_data.get('restaurant_name')
        if name and len(name) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres')
        return name
    
    # Validación personalizada de precio
    def clean_average_price(self):
        price = self.cleaned_data.get('average_price')
        if price and price < 0:
            raise ValidationError('El precio no puede ser negativo')
        return price