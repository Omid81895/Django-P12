from django.shortcuts import render
from .form import BookForm
from .models import Book
# Create your views here.
def main(request):
    books = Book.objects.all()
    return render(request, 'library/main.html', {'books':books})
def add(request):
    pass
def change(request, id):
    pass
def delete(request, id):
    pass
def filter_priority(request):
    pass
def filter_read(request):
    pass