from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ("author","isbn")