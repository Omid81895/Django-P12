from django.shortcuts import render, redirect
from .form import BookForm
from django.http import HttpResponseRedirect
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
    if request.method == "POST":
        form = BookForm(request.POST ,instance =book)
        if form.is_valid():
            cd = form.cleaned_data
            book.title = cd['title']
            book.author = cd['author']
            book.priority = cd['priority']
            book.read_status = cd['read_status']
            book.note = cd['note']
            book.delete()
            return redirect('main')
    else:
        form = BookForm(instance=book)
        return render(request, 'library/delete.html', {'form': form})
def filter_read(request):
    books = Book.objects.all().order_by('read_status')
    return render(request,'library/filter_read.html', {'books':books})