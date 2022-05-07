from dataclasses import fields
from django import forms
from .models import Post

class ListForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content","image",]