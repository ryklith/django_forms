from django import forms
from .models import CompetitionRequest


class CompetitionRequestForm(forms.ModelForm):
    class Meta:
        model = CompetitionRequest
        fields = '__all__'

