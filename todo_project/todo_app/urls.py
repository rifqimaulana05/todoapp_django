from django.urls import path, include
from .views import LandingView, TodoDetailView, TodoListView

urlpatterns = [
    path('books/', include('books.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', LandingView.as_view(), name='landing'),
    # path('todo/', TodoListView.as_view(), name='todo_list'),
    # path('todo/<int:todo_id>/', TodoDetailView.as_view(), name='todo_detail'),
]