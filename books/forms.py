from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kitob nomi'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Muallif'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tavsif', 'rows': 4}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
