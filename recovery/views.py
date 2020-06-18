from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def Home(request):
    return render(request, 'recovery/home.html')

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'recovery/register.html', {'form': form})

def Login(request):
    return render(request, 'recovery/login.html')