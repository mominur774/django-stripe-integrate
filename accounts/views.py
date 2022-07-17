from django.shortcuts import redirect, render
from accounts.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created!")
            return redirect('/accounts/login')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']

            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('/')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('/accounts/login/')
