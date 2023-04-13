from . import views
from django.urls import path
from .views import HomeView, ArticuloDetalleVista, Agregar_Post, UpdatePost, EliminarPost, CategoriasView

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('articulo/<int:pk>', ArticuloDetalleVista.as_view(), name = "articulodetalle"),
    path('agregar_post/', Agregar_Post.as_view(), name = "agregar_post"),
    path('articulo/editar/<int:pk>', UpdatePost.as_view(), name = "editar_post"),
    path('articulo/eliminar/<int:pk>', EliminarPost.as_view(), name = "eliminar_post"),
    path('categorias/<str:cat>/', CategoriasView, name = "categorias"),
]