from django import forms
from .models import Post

class PostForms(forms.ModelForm):
    """docstring for PostForms"""
    class Meta:
        model = Post
        fields = ('title','text',)
