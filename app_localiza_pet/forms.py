from django import forms
from .models import Animal_post


class AmimalPostForm(forms.ModelForm):
    class Meta:
        model = Animal_post
        fields = ['foto', 'opcao', 'descricao', 'user']
