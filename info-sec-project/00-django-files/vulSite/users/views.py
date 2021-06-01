from django.shortcuts import render, redirect


def login_func(request):
    data = {}
    return render(request, "login.html", data)
