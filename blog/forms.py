from django import forms

from .models import Post, Ipost, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class IpostForm(forms.ModelForm):

    class Meta:
        model = Ipost
        fields = ('title', 'text','images',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
