from .models import Book
from .views import get_cookie
def read_status(request):
    
    return {'status_choices': Book.READING}

def theme(request):
        return{'theme': request.COOKIES.get('theme', 'light')}
