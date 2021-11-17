from django.urls import path
from django.contrib.auth import views as auth_views
from Cadastros.views import PessoasCreate
from Cadastros.views import PessoasUpdate

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="usuarios/login.html"),
        name="login",
    ),
    path("registrar/", PessoasCreate.as_view(), name="registrar"),
    path("atualizar-dados/", PessoasUpdate.as_view(), name="atualizar-dados"),
]
