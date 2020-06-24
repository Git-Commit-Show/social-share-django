from django import forms
from .models import addText


class addTextForm(forms.ModelForm):
    class Meta:
        model= addText
        fields= ["text", "position"]
