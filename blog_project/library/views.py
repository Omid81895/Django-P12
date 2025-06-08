from django.shortcuts import render, redirect
from .form import BookForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Book
# Create your views here.
def main(request):
    books = Book.objects.all()
    return render(request, 'library/main.html', {'books':books})
def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'library/add.html', {'form': form})
    else:
        form = BookForm()
    return render(request, 'library/add.html', {'form': form})
def change(request, id):
    book = Book.objects.get(id = id)
    if request.method == "POST":
        form = BookForm(request.POST ,instance =book)
        if form.is_valid():
            form.save()
        return redirect('main')
    else:
        form = BookForm(instance=book)
        return render(request, 'library/change.html', {'form': form})
def delete(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    return redirect('main')
    
def filter_read(request,read_status):
    books = Book.objects.filter(read_status = read_status)
    return render(request,'library/filter_read.html', {'books':books})
def set_cookie(request):
    response = render(request, 'templates/base.html')
    response.set_cookie('theme', 'light')
    return response
def get_cookie(request):
    theme = request.COOKIES['theme']
    return redirect('main')