from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.utils import timezone
from datetime import timedelta

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = timezone.now() + timedelta(days=7)
        super().save(*args, **kwargs)

    def days_late(self):
        if self.return_date and self.return_date > self.due_date:
            return (self.return_date - self.due_date).days
        return 0

    def fine(self):
        return self.days_late() * 2000
