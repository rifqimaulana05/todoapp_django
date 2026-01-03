from django.urls import path
from .views import book_list, index

urlpatterns = [
    path('', index, name='index'),
    path('books/', book_list, name='book_list'),
]
