from django.urls import path
from .views import book_list, book_create, book_update, book_delete

urlpatterns = [
    path('', book_list, name='book_list'),
    path('new/', book_create, name='book_create'),
    path('<int:pk>/edit/', book_update, name='book_update'),
    path('<int:pk>/delete/', book_delete, name='book_delete'),
]

from django.contrib import admin
from django.urls import path, include  # `include` ni import qilish kerak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('http://127.0.0.1:8000')),  # books ilovasining URL-larini bog‘lash
]

