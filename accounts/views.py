from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignUpForm, AuthenticationForm

# Registro

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        user_signup_form = UserSignUpForm(request.POST)
        if user_signup_form.is_valid():
            user_signup_form.save()
            return render(request, "accounts/signup_success.html", {"user" : user_signup_form.cleaned_data.get("username")})
    else:
        user_signup_form = UserSignUpForm()
    return render(request, "accounts/signup.html", {"form" : user_signup_form})

# Login

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "accounts/login_success.html", {})
        else:
            user_login_form = AuthenticationForm()
            return render(request, "accounts/login.html", {"form" : user_login_form, "error_login" : True})
    user_login_form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form" : user_login_form, "error_login" : False})

# Logout

def user_logout(request):
    logout(request)
    return render(request, "accounts/logout.html", {})