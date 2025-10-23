from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Category, MenuItem
from .forms import CategoryForm, MenuItemForm

def home(request):
    return HttpResponse("Hello, welcome to the first Django app!")

def display_date(request):
    import datetime
    now = datetime.datetime.now()
    html = f"<html><body>Current date and time: {now}</body></html>"
    return HttpResponse(html)

def req_path(request):
    path = request.path
    return HttpResponse(path, content_type="text/html", charset="utf-8")

def params_example(request, param1, param2):
    return HttpResponse(f"Parameter 1: {param1}, Parameter 2: {param2}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"Artículo: {slug} — Fecha: {month}/{year}")

# ============= VISTAS DE CATEGORÍAS =============

def category_list(request):
    """Lista todas las categorías"""
    categories = Category.objects.all()
    return render(request, 'first_app/category_list.html', {
        'categories': categories
    })

def category_create(request):
    """Crear una nueva categoría"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Categoría "{category.name}" creada exitosamente.')
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    return render(request, 'first_app/category_form.html', {
        'form': form,
        'title': 'Crear Categoría',
        'button_text': 'Crear'
    })

def category_update(request, pk):
    """Editar una categoría existente"""
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Categoría "{category.name}" actualizada exitosamente.')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'first_app/category_form.html', {
        'form': form,
        'title': f'Editar Categoría: {category.name}',
        'button_text': 'Actualizar'
    })

def category_delete(request, pk):
    """Eliminar una categoría"""
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'Categoría "{category_name}" eliminada exitosamente.')
        return redirect('category_list')
    
    return render(request, 'first_app/category_confirm_delete.html', {
        'category': category
    })

# ============= VISTAS DE PLATOS DEL MENÚ =============

def menu_list(request):
    """Lista todos los platos del menú"""
    menu_items = MenuItem.objects.select_related('category').all()
    
    # Filtros opcionales
    category_id = request.GET.get('category')
    if category_id:
        menu_items = menu_items.filter(category_id=category_id)
    
    available_only = request.GET.get('available')
    if available_only == '1':
        menu_items = menu_items.filter(is_available=True)
    
    categories = Category.objects.all()
    
    return render(request, 'first_app/menu_list.html', {
        'menu_items': menu_items,
        'categories': categories
    })

def menu_create(request):
    """Crear un nuevo plato del menú"""
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save()
            messages.success(request, f'Plato "{menu_item.name}" creado exitosamente.')
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    
    return render(request, 'first_app/menu_form.html', {
        'form': form,
        'title': 'Crear Plato',
        'button_text': 'Crear'
    })

def menu_update(request, pk):
    """Editar un plato del menú existente"""
    menu_item = get_object_or_404(MenuItem, pk=pk)
    
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Plato "{menu_item.name}" actualizado exitosamente.')
            return redirect('menu_list')
    else:
        form = MenuItemForm(instance=menu_item)
    
    return render(request, 'first_app/menu_form.html', {
        'form': form,
        'title': f'Editar Plato: {menu_item.name}',
        'button_text': 'Actualizar'
    })

def menu_delete(request, pk):
    """Eliminar un plato del menú"""
    menu_item = get_object_or_404(MenuItem, pk=pk)
    
    if request.method == 'POST':
        menu_item_name = menu_item.name
        menu_item.delete()
        messages.success(request, f'Plato "{menu_item_name}" eliminado exitosamente.')
        return redirect('menu_list')
    
    return render(request, 'first_app/menu_confirm_delete.html', {
        'menu_item': menu_item
    })

def menu_detail(request, pk):
    """Ver detalles de un plato del menú"""
    menu_item = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'first_app/menu_detail.html', {
        'menu_item': menu_item
    })

# ============= VISTA PRINCIPAL =============

def home(request):
    """Página de inicio con estadísticas"""
    categories_count = Category.objects.count()
    menu_items_count = MenuItem.objects.count()
    available_items = MenuItem.objects.filter(is_available=True).count()
    
    return render(request, 'first_app/home.html', {
        'categories_count': categories_count,
        'menu_items_count': menu_items_count,
        'available_items': available_items,
    })
    """
    Vista alternativa que muestra el formulario sin template
    (solo para demostración, no es la mejor práctica)
    """
    
    if request.method == 'POST':
        form = RestaurantRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Crear respuesta HTML simple
            html = "<html><body>"
            html += "<h1>✅ Formulario enviado exitosamente</h1>"
            html += "<h2>Datos recibidos:</h2><ul>"
            
            for field, value in form.cleaned_data.items():
                if field != 'password' and field != 'password_confirm':
                    html += f"<li><strong>{field}:</strong> {value}</li>"
            
            html += "</ul>"
            html += '<a href="/restaurant-form/">Volver al formulario</a>'
            html += "</body></html>"
            
            return HttpResponse(html)
        else:
            # Mostrar errores
            html = "<html><body>"
            html += "<h1>❌ Errores en el formulario</h1>"
            html += "<ul>"
            for field, errors in form.errors.items():
                html += f"<li><strong>{field}:</strong> {', '.join(errors)}</li>"
            html += "</ul>"
            html += '<a href="/restaurant-form/">Volver</a>'
            html += "</body></html>"
            return HttpResponse(html)
    
    else:
        form = RestaurantRegistrationForm()
        
        # Renderizar formulario manualmente (no recomendado)
        html = """
        <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <h1>Registro de Restaurante</h1>
                <form method="post" enctype="multipart/form-data">
        """
        
        # Django requiere el token CSRF para seguridad
        from django.middleware.csrf import get_token
        html += f'<input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}">'
        
        # Renderizar cada campo del formulario
        html += str(form.as_p())
        
        html += """
                    <button type="submit" class="btn btn-primary">Enviar</button>
                </form>
            </div>
        </body>
        </html>
        """
        
        return HttpResponse(html)