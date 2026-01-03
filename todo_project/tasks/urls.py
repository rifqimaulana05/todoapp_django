from django.urls import path
from .views import task_list, task_create, task_toggle, task_delete, task_update

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', task_create, name='task_create'),
    path('edit/<int:id>/', task_update, name='task_update'),
    path('delete/<int:id>/', task_delete, name='task_delete'),
    path('toggle/<int:task_id>/', task_toggle, name='task_toggle'),
]
