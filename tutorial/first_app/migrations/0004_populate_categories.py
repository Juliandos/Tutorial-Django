from django.db import migrations

def create_categories_and_assign(apps, schema_editor):
    Menu = apps.get_model('first_app', 'Menu')
    MenuCategory = apps.get_model('first_app', 'MenuCategory')
    
    # Crear una categoría por defecto usando el campo correcto: menu_category_name
    default_category = MenuCategory.objects.create(
        menu_category_name="Categoría Por Defecto"
    )
    
    # Asignar todos los elementos de menú existentes a la categoría por defecto
    Menu.objects.filter(category_id__isnull=True).update(category_id=default_category)
    
    print(f"Categoría creada: {default_category.menu_category_name}")
    print(f"Menús actualizados: {Menu.objects.filter(category_id=default_category).count()}")

def reverse_populate(apps, schema_editor):
    # Para revertir: eliminar las categorías
    MenuCategory = apps.get_model('first_app', 'MenuCategory')
    MenuCategory.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('first_app', '0003_add_menucategory_nullable'),
    ]

    operations = [
        migrations.RunPython(create_categories_and_assign, reverse_populate),
    ]
