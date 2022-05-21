from logging import PlaceHolder
from tkinter.ttk import Widget
from xml.parsers.expat import model
from django.forms import ModelForm, Textarea, TextInput, Select
from .models import Bb

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ['title', 'content', 'rubric']

        widgets = {

            'title' : TextInput(attrs={
                'class' : 'form-control',
                'PlaceHolder' : 'Title of article',
            }),
            'content' : Textarea(attrs={
                'class' : 'form-control',
                'PlaceHolder' : 'Content of article',
                'rows' : '10'
            }),
            'rubric' : Select(attrs={
                'class' : 'form-select',
            })

            }