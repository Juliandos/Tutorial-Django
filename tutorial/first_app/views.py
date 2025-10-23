from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

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