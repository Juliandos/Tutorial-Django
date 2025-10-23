from django.urls import path, re_path
from first_app import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('date/', views.display_date, name='display_date'),
    path('path/', views.req_path, name='req_path'),
    path('params/<str:param1>/<str:param2>/', views.params_example, name='params_example'),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),
    # Página principal
    path('', views.home, name='home'),
    
    # URLs de Categorías
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # URLs de Platos del Menú
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/create/', views.menu_create, name='menu_create'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('menu/<int:pk>/update/', views.menu_update, name='menu_update'),
    path('menu/<int:pk>/delete/', views.menu_delete, name='menu_delete'),
]