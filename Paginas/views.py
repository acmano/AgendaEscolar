from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "Paginas/index.html"


class SobreView(TemplateView):
    template_name = "Paginas/sobre.html"
