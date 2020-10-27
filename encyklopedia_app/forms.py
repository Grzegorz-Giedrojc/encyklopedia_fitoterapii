from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('autor', 'nazwa', 'opis', 'choroby', 'zastosowanie', 'zdjecie', 'created_date', 'published_date',)
