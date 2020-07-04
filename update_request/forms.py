from django.forms import ModelForm
from django import forms

from .models import UpdateRequest


class UpdateForm(ModelForm):

    project = forms.ChoiceField(label="Projeto")
    branch_name = forms.CharField(max_length=100, label="Nome da branch")
    description = forms.CharField(max_length=100, label="Descrição")

    class Meta:
        model = UpdateRequest
        fields = ["project", "branch_name", "description"]
