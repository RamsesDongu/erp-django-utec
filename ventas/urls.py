# ventas/urls.py
"""URLs de la app ventas — W12 (con endpoint PDF)."""
from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    # Lectura
    path('', views.VentaListView.as_view(), name='lista'),
    path('<int:venta_id>/', views.VentaDetailView.as_view(), name='detalle'),
    # Escritura
    path('nueva/', views.crear_venta, name='crear'),
    path('<int:venta_id>/eliminar/', views.VentaDeleteView.as_view(), name='eliminar'),
    # Documentos (W12)
    path('<int:venta_id>/pdf/', views.venta_pdf, name='pdf'),
]