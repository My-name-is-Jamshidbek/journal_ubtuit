from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import UserRegistrationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your homepage URL pattern
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(1)
        if form.is_valid():
            print(1)
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your homepage URL pattern
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the name of your homepage URL pattern
