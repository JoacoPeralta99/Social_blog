from django import forms
from social.models import Post

class PostForm(forms.ModelForm):
    tittle = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':1,'placeholder': 'nombre publicacion...'}),required = True)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2,'placeholder': 'que quieres contar...'}),required = True)

    class Meta:
        model = Post
        fields = ['tittle','content']
