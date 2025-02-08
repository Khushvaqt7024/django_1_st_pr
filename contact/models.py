from django.utils import timezone

from django.core.exceptions import ValidationError
from django.db import models

def validate_full_name(value):
    if len(value) < 1:
        raise ValidationError('Please enter a name')

class Author(models.Model):
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=13)
    nationality = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    description = models.TextField(default='Hech narsa yoq')
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    # price = models.IntegerField()


    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)



