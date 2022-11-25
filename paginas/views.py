from django.shortcuts import render
from django.views.generic import TemplateView



class PaginaPrincipal(TemplateView):
    template_name = 'modelo.html'

class Sobre(TemplateView):
    template_name = 'sobre.html'