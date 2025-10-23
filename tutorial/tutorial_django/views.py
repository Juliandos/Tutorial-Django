from django.http import HttpResponse, HttpResponseNotFound

def custom_404_view(request, exception):
    return HttpResponse("""
        <div style="text-align:center; font-family:Arial; margin-top:100px;">
            <h1 style="color:#e74c3c;">404 - Page Not Found</h1>
            <p>The page you are looking for doesn’t exist.</p>
            <a href="/" 
               style="display:inline-block; margin-top:20px; padding:10px 20px; 
                      background-color:#3498db; color:white; text-decoration:none; 
                      border-radius:5px;">
               Go Back Home
            </a>
        </div>
    """, status=404)

# def home(request):
#     return HttpResponseNotFound("Home view as 404 handler")