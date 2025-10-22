from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('date/', views.display_date, name='display_date'),
    path('path/', views.req_path, name='req_path'),
    path('params/<str:param1>/<str:param2>/', views.params_example, name='params_example'),
]