from django import forms

from .models import Post
from .models import Ipost

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class IpostForm(forms.ModelForm):

    class Meta:
        model = Ipost
        fields = ('title', 'text','images',)
