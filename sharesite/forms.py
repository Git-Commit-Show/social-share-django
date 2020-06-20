from django import forms

from .models import PostData

class PostForm(forms.ModelForm):

    class Meta:
        model = PostData
        fields = ('text','hashTags','url')