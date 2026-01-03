from django.urls import path
from .views import borrow_book, loan_history

urlpatterns = [
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('history/', loan_history, name='loan_history'),

]
