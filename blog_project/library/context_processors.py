from .models import Book

def read_status(request):
    
    return {'status_choices': Book.READING}