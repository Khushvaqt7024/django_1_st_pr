from django.urls import path, include
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),  # 🔧 id -> pk o‘zgartirildi
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    # 🔐 Login, Logout va Signup URL-lar
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
]