from django import forms
from .models import Book
from django.core import validators
class BookForm(forms.ModelForm):
    note = forms.CharField(required=False,widget=forms.Textarea({'class': 'form-control'}),help_text='(This part is optional.)')
    class Meta:
        model = Book 
        fields = ['title', 'author', 
                  'read_status', 'note', 'priority']
        labels = {
            'title': 'Title of the Book',
            'author': 'Who wrote this?',
        }
        widgets = {
            'title': forms.TextInput({
                'class': 'form-control'
            }),
            'author': forms.TextInput({
                'class': 'form-control'
            }),
            'read_status' : forms.RadioSelect(
                attrs={'class': 'form-check-input'}),
            'priority': forms.RadioSelect(
                attrs={'class': 'form-check-input'})
            
        }