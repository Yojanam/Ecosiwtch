from django.shortcuts import render
from django.views.generic import TemplateView

# Creat e your views here.

class HomePageView(TemplateView):
    template_name = 'core/index.html',
    datos = {'saludo': 'Hola'}



    dict_context = {
        'tittle': 'Inicio',
        'message': 'Bienvenido a mi sitio web',
        'datos': datos,
    }

    def get(self, request, *args, **kwargs):
        #Metodo que se encarga de devolver la vista
        return render(request, self.template_name, self.dict_context)
    

class AdvantageView(TemplateView):
    template_name = 'core/ventajas.html'

    dict_context = {
        
    }