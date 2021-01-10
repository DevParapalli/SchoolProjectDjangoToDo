
from django import forms
from django.forms import widgets
from .models import ToDo
from simple_todo import settings

class ToDoForm(forms.ModelForm):
    dead_line = forms.DateTimeField(input_formats=settings.DATE_TIME_INPUT_FORMATS)
    
    class Meta:
        model=ToDo
        fields=('title', 'data', 'dead_line')
        excludes=("updated_date_time",)
        widgets = {
            'dead_line': widgets.DateTimeInput(attrs={'required': True, 'placeholder':'DD/MM/YYYY HH:MM[:SS]'})
        }

class ToDoEditForm(forms.ModelForm):
    dead_line = forms.DateTimeField(input_formats=settings.DATE_TIME_INPUT_FORMATS)
    
    class Meta:
        model = ToDo
        fields=('title', 'data', 'dead_line')
        excludes=("updated_date_time",)