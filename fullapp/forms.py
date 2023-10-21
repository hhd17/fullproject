from django import forms
from .models import Book

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class FibonacciForm(forms.Form):
    number = forms.IntegerField(label='Enter a number')
    