from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

def login_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('task_list')

    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            
            user.is_staff = False
            user.is_superuser = False
            user.save()

            return redirect('login')
    else:
        form = UserCreationForm()
    print("🔥 REGISTER VIEW DIPANGGIL 🔥")
    return render(request, 'registration/registrasi.html', {'form': form})
