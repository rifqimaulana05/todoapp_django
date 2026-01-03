from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from books.models import Book
from .models import Loan

# Create your views here.

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # validasi: stok habis
    if book.stock <= 0:
        messages.error(request, "Stok buku habis.")
        return redirect('book_list')

    # validasi: user tidak boleh pinjam buku yang sama
    already_borrowed = Loan.objects.filter(
        user=request.user,
        book=book,
        is_returned=False
    ).exists()

    if already_borrowed:
        messages.warning(request, "Kamu sudah meminjam buku ini.")
        return redirect('book_list')

    # proses pinjam
    Loan.objects.create(user=request.user, book=book)
    book.stock -= 1
    book.save()

    messages.success(request, "Buku berhasil dipinjam.")

    # 🔴 INI PENTING
    return redirect('loan_history') 

@login_required
def loan_history(request):
    loans = Loan.objects.filter(user=request.user)
    return render(request, 'loans/history.html', {'loans': loans})
