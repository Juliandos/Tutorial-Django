from django.http import HttpResponse, HttpResponseNotFound

def custom_404_view(request, exception):
    return HttpResponse("Custom 404 Page Not Found", status=404)

# def home(request):
#     return HttpResponseNotFound("Home view as 404 handler")