from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    """Categoría de platos del menú"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre de la categoría"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Plato del menú del restaurante"""
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre del plato"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_items',
        verbose_name="Categoría"
    )
    description = models.TextField(
        verbose_name="Descripción",
        help_text="Describe los ingredientes y preparación"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Precio"
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Disponible"
    )
    is_vegetarian = models.BooleanField(
        default=False,
        verbose_name="Vegetariano"
    )
    spicy_level = models.IntegerField(
        choices=[
            (0, 'No picante'),
            (1, 'Poco picante'),
            (2, 'Medio picante'),
            (3, 'Muy picante'),
        ],
        default=0,
        verbose_name="Nivel de picante"
    )
    preparation_time = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Tiempo en minutos",
        verbose_name="Tiempo de preparación"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Plato del menú"
        verbose_name_plural = "Platos del menú"
        ordering = ['category', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.category.name}"