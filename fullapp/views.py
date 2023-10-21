from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBookForm, FibonacciForm
from .models import Book

def home(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('success', book_id=book.id)
    else:
        form = CreateBookForm()
    return render(request, 'fullapp/createbook.html', {'form': form})

def success(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'fullapp/success.html', {'book': book})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = CreateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('success', book_id=book.id)
    else:
        form = CreateBookForm(instance=book)
    return render(request, 'fullapp/editbook.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('home')

def fibonacci(request):
    result = None
    if request.method == 'POST':
        form = FibonacciForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['number']
            result = fib(num)
    else:
        form = FibonacciForm()
    return render(request, 'fullapp/fibonacci.html', {'form': form, 'result': result})

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
