from django import forms
from ..models import Category

class CategoryForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}),label='Descripción')  


    class Meta:
        model = Category
        fields = ['name','description']

        labels = {
                'name': 'Nombre',  
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'Titulo de categoria'})
        self.fields['description'].widget.attrs.update({'class':'form-control form-control-lg','placeholder':'Contenido'})
        
