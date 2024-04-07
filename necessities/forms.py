from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Necessities


class NecessitiesForm(forms.ModelForm):
    class Meta:
        model = Necessities
        fields = ['title', 'description']
        widgets = {
            'description': CKEditorWidget(),
        }
