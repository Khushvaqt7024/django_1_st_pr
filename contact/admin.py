from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    pass