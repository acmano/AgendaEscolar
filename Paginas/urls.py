from django.urls import path
from .views import PaginaInicial, SobreView

urlpatterns = [
    # path('endereco/', MinhaView.as_View(), nome='nome-da-url'),
    path("", PaginaInicial.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),
]
