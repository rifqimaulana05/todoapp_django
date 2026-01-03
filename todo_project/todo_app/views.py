from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def admin_dashboard(request):
    if request.user.profile.role != 'admin':
        return HttpResponse("Unauthorized", status=401)
    return render(request, 'admin_dashboard.html')

# Create your views here.
class LandingView(View):
    def get(self, request):
        return render(request, 'landing.html')
    
class TodoListView(View):
    def get(self, request):
        return render(request, 'todo_list.html')
    
class TodoDetailView(View):
    def get(self, request, todo_id):
        return render(request, 'todo_detail.html', {'todo_id': todo_id})