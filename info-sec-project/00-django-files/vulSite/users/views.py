from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

# from .models import User


def login_func(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # login code
        data.update({"username": username})
        print(username)
        print(password)

    for i in User.objects.raw("select id, username, password from auth_user"):
        print(i.id, i.username, i.password)

    return render(request, "login.html", data)


def logout(request):
    auth_logout(request)
    return redirect("http://127.0.0.1:8000/auth/")
