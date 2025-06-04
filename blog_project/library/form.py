from django import forms
from .models import Book
from django.core import validators
class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        READING = (
            ('' , "How much did you read this book?"),
            ('D', "Done"),
            ('SR' , "Still Reading"),
            ('NR' , "Not Read")
        )
        RANKING = (
            ('', 'Pick your priority'),
            (1 , 'High') ,
            (2 ,'MEDIUM' ) ,
            (3 , 'LOW') ,
        )
        fields = ['title', 'author', 
                  'read_status', 'note', 'priority']
        labels = {
            'title': 'Title of the Book',
            'author': 'Who wrote this?',
        }
        help_texts ={
            'note': '(This part is optional.)'
        }
        widgets = {
            'title': forms.TextInput({
                'class': 'form-control'
            }),
            'author': forms.TextInput({
                'class': 'form-control'
            }),
            'read_status' : forms.ChoiceField(),
            'note': forms.Textarea({
                'class': 'form-control'
            }),
            'priority': forms.ChoiceField()
            
        }