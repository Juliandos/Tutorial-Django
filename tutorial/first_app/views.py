from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RestaurantRegistrationForm
import json

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

def restaurant_form_view(request):
    """
    Vista que maneja el formulario de registro de restaurante
    
    Flujo:
    - GET: Muestra el formulario vacío
    - POST: Procesa los datos enviados
    """
    
    if request.method == 'POST':
        # Crear instancia del formulario con los datos enviados
        form = RestaurantRegistrationForm(request.POST, request.FILES)
        
        # Validar el formulario
        if form.is_valid():
            # Los datos validados están en form.cleaned_data
            data = form.cleaned_data
            
            # Aquí puedes procesar los datos:
            # - Guardar en base de datos
            # - Enviar email
            # - Realizar cálculos
            # etc.
            
            # Ejemplo: Guardar la información
            restaurant_info = {
                'nombre': data['restaurant_name'],
                'email': data['email'],
                'año': data['year_established'],
                'precio_promedio': str(data['average_price']),
                'rating': data['rating'],
                'país': data['country'],
                'descripción': data['description'],
                'delivery': data['has_delivery'],
                'servicios': data['services'],
                'reservación': data['reservation_required'],
                'fecha_apertura': str(data['opening_date']),
                'hora_apertura': str(data['opening_time']),
                'website': data['website'],
                'categoría': str(data['menu_category']),
            }
            
            # Manejar archivo de imagen
            if data['logo']:
                # En producción, guardarías el archivo
                restaurant_info['logo'] = data['logo'].name
            
            # Mostrar página de éxito
            return render(request, 'first_app/success.html', {
                'restaurant_info': restaurant_info
            })
        
        else:
            # El formulario tiene errores, se volverá a mostrar con los errores
            pass
    
    else:
        # GET: Mostrar formulario vacío
        form = RestaurantRegistrationForm()
    
    # Renderizar el template con el formulario
    return render(request, 'first_app/restaurant_form.html', {
        'form': form
    })

def restaurant_form_simple_view(request):
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