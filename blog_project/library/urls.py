from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('add/', views.add, name = 'add'),
    path('change/<int:id>', views.change, name = 'change'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('read/<str:read_status>', views.filter_read, name = 'read'),
    path('set/', views.set_cookie, name = 'set')
]