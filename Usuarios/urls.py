from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PessoaUpdate

urlpatterns = [
    # path('', view, name=""),
    #    path(
    #        "login/",
    #        auth_views.LoginView.as_view(template_name="usuarios/login.html"),
    #        name="login",
    #    ),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="Paginas/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registrar/", UsuarioCreate.as_view(), name="registrar"),
    path("atualizar-dados/", PessoaUpdate.as_view(), name="atualizardados"),
]
