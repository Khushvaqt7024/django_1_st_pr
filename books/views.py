from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Bosh sahifa - Kitoblar ro'yxati (Qidiruv va Pagination bilan)
@login_required(login_url="")
def book_list(request):
    query = request.GET.get('q', '')  # 🔍 Qidiruv so'rovi (bo‘sh qiymat agar yo‘q bo‘lsa)
    books = Book.objects.all().order_by('-published_date')

    if query:
        books = books.filter(title__icontains=query)  # 📚 Sarlavhaga ko‘ra qidirish

    # Pagination - Har bir sahifada 5 ta kitob ko‘rsatiladi
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'book/book_list.html', context)


#  Yangi kitob qo'shish
@login_required
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('library:book_list')
    return render(request, 'book/book_form.html', {'form': form})


#  Kitobni tahrirlash
@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('library:book_list')
    return render(request, 'book/book_form.html', {'form': form})


# Kitobni o'chirish
@login_required
def book_delete(request, pk):
    print('book delete ', pk)
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('library:book_list')


# Aloqa sahifasi
def contact(request):
    return render(request, 'book/contact_book.html')


# Biz haqimizda sahifasi
def about(request):
    return render(request, 'book/about.html')


# Ro‘yxatdan o‘tish (Signup) funksiyasi
def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('library:book_list')
    return render(request, 'registration/signup.html', {'form': form})
