
from django import forms
from models import Contact

class PostForm(forms.ModelForm):
    class Meta:
        model = Contact
        # exclude = ['author', 'updated', 'created', ]
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={
                'id': 'nom',
                'required': True,
                'placeholder': 'Say something...'
            }),
        }