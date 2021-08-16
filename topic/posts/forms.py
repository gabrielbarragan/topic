"""Post forms"""

#django 
from django import forms

#models
from posts.models import Post

class PostForm (forms.ModelForm):
    """Post model form."""
    class Meta:
        """Form settings"""
        model = Post
        fields = ['user','Profile','title','photo']
