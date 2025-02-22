from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('book.urls')),
]

from django.urls import path
from .views import book_list, book_create, book_update, book_delete

urlpatterns = [
    path('', book_list, name='book_list'),
    path('', book_create, name='book_create'),
    path('', book_update, name='book_update'),
    path('', book_delete, name='book_delete'),
]
