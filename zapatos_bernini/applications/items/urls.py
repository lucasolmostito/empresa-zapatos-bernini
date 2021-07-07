from django.urls import path

from . import views

app_name = 'app_items'

urlpatterns = [
    path('agregar-articulo/', views.AddItemFormView.as_view(), name='add-item'),
    path('restar-articulo/<pk>/', views.SubtractQuantityItemView.as_view(), name='subtract-item'),
    path('sumar-articulo/<pk>/', views.AddQuantityItemView.as_view(), name='add-item'),
    path('eliminar-articulo/<pk>/', views.ItemCartDeleteView.as_view(), name='delete-item'),
    path('api/articulos-lista/', views.ItemsListApiView.as_view()),
    path('api/articulo-detalle/<pk>/', views.ItemDetailApiView.as_view()),
]
