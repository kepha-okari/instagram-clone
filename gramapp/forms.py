from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Image,Comment


class ImagePostForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create Post
    '''
    class Meta:
        model = Image
        fields = ['image','image_name', 'image_caption']

class CommentForm(forms.ModelForm):
    '''
    class that creates the comment form
    '''
    class Meta:
        model = Comment
        fields = ['comment']
