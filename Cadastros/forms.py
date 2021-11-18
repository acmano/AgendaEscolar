from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        e = self.cleaned_data["email"]
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e


from .models import Agendas, AgendasRecados


class AgendaForm(forms.Form):
    agenda = forms.ModelChoiceField(queryset=Agendas.objects.all())

    class Meta:
        model = Agendas, AgendasRecados
        fields = ["TurmaProfessor", "Matricula", "Data"]
