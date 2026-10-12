
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Páginas web existentes
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('destinos/', views.destinos_list, name='destinos'),
    path('crear/', views.crear_destino, name='crear'),
    path('editar/<int:id>/', views.editar_destino, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_destino, name='eliminar'),

    # API REST
    path('api/destinos/', views.api_destinos, name='api_destinos'),
    path('api/destinos/<int:id>/', views.api_destino_detalle, name='api_destino_detalle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
