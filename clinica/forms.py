from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome','cpf', 'genero','aniversario','empresa',
                  'cep','rua','numero','bairro','cidade','estado',
                  'foto')