from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/<int:id>/', views.book, name='book'),
    path('books/<int:id>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:id>/delete/', views.book_delete, name='book_delete'),
]
if settings.DEBUG:


import django.contrib
from django.urls import path, include  # include ni import qiling

urlpatterns = [
    path('admin/', django.contrib.admin.site.urls),
    path('books/', include('books.urls')),  # books ilovasining URL-larini qo'shish
]
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]