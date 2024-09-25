from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('actualizar/<int:id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('cuenta/<int:usuario_id>/', views.cuenta_usuario, name='cuenta_usuario'),
]
