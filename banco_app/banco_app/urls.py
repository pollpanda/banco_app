from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/cuenta/<int:usuario_id>/', views.cuenta_usuario, name='cuenta_usuario'),
    # Otras rutas de tu app
]
