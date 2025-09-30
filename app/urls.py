from django.urls import path
from .views import (
    HomeView,
    UsuarioListView,
    UsuarioDetailView,
    UsuarioCreateView,
    UsuarioDeleteView,
    UsuarioUpdateView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('usuarios/', UsuarioListView.as_view(), name='listar_usuarios'),
    path('usuarios/<int:usuario_id>/', UsuarioDetailView.as_view(), name='detalhes_usuario'),
    path('usuarios/novo/', UsuarioCreateView.as_view(), name='criar_usuario'),
    path('usuarios/<int:usuario_id>/delete/', UsuarioDeleteView.as_view(), name='delete_usuario'),
    path('usuarios/<int:usuario_id>/edit/', UsuarioUpdateView.as_view(), name='editar_usuario'),
]