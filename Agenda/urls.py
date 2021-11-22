"""
    [summary]
    [extended_summary]
    Returns:
        [type]: [description]
"""
from django.urls import path

from Agenda.views import lista, inserir, editar

urlpatterns = [
    path("lista/", lista, name="agenda_lista"),
    path("inserir/", inserir, name="agenda_inserir"),
    path("editar/<int:pk>/", editar, name="agenda_editar"),
]
