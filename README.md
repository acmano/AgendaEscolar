mkkdir AgendaEscolar
cd AgendaEscolar
git init (inicia o repositório git)
conda create --name VEnvAE python=3.10 (criar ambiente virtual para python 3.10, com nome VEnvAE)
conda activate VEnvAE (ativa o ambiente virtual)
code . (abre VSCode na pasta do projeto)
criar arquivo \requirements.txt: (para informar as bibliotecas, frameworks e pacotes de terceiros necessários ao projeto)
  django==3.2.9
  django-autoslug==1.9.8
  django-debug-toolbar==3.2.2
  django-model-utils==4.2.0
  factory-boy==3.2.1
  ipython==7.29.0
  pytest==6.2.5
  pytest-cov==3.0.0
  pytest-django==4.4.0
pip install -r requirements.txt
pip install --upgrade pillow --global-option="build_ext" --global-option="--disable-jpeg" --global-option="--disable-zlib"
pip install --only-binary :all: mysqlclient
criar arquivo \.gitignore  (para python())
django-admin.exe startproject AgendaEscolar . (cria o projeto)
git add .
git commit -m "Início do projeto"
python manage.py startapp users (cria o app users)
del sqlite3
del users\tests.py
mkdir users\tests
criar users\tests\__init__.py (vazio)
criar users\tests\test_models.py
  import pytest
  from ..models import User
  pytestmark = pytest.mark.django_db
  def test_create_user():
    user = User.objects.create_user(
      username="usuario_test", email="usuario@test.com", password="passw0rd"
    )
    assert user.username == "usuario_test"
    assert user.email == "usuario@test.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
  def test_create_superuser():
    user = User.objects.create_superuser(
      username="admin_test", email="admin@test.com", password="passw0rd"
    )
    assert user.username == "admin_test"
    assert user.email == "admin@test.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser
criar \pytest.ini:
  [pytest]
    DJANGO_SETTINGS_MODULE = AgendaEscolar.settings
criar \.coveragerc:
  [run]
  omit =
    *migrations*,
    *tests*,
    AgendaEscolar*,
    conftest.py

CREATE DATABASE AgendaEscolar CHARACTER SET utf8 COLLATE utf8_general_ci ;
CREATE USER 'AEadmin' IDENTIFIED BY 'AEpass01!" ;
grant all privileges on AgendaEscolar.* to 'AEadmin' with grant option ;
python .\manage.py createsuperuser
  AEadmin
  antonio.mano@gmail.com
  AEpass01!