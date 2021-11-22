from django.urls import path
from .views import PaginaInicial, SobreView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('endereco/', MinhaView.as_View(), nome='nome-da-url'),
    path("", PaginaInicial.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    path("sobre/", SobreView.as_view(), name="agenda-dados"),
    path("sobre/", SobreView.as_view(), name="password"),
]
