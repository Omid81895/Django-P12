from django.shortcuts import render
from .form import BookForm
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
    pass
def delete(request, id):
    pass
def filter_priority(request):
    pass
def filter_read(request):
    pass