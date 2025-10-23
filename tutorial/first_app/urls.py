from django.urls import path, re_path
from first_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('date/', views.display_date, name='display_date'),
    path('path/', views.req_path, name='req_path'),
    path('params/<str:param1>/<str:param2>/', views.params_example, name='params_example'),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),
]