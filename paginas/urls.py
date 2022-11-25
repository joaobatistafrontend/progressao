from django.urls import path
from .views import PaginaPrincipal,Sobre


urlpatterns = [
    path('',PaginaPrincipal.as_view(),name='index'),
    path('sobre/',Sobre.as_view(),name='sobre'),
]
 