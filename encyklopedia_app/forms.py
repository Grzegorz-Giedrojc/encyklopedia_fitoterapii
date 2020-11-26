from django import forms

from .models import Post



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('autor', 'nazwa', 'opis', 'choroby', 'zastosowanie', 'zdjecie', 'created_date', 'published_date',)

def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])
