from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    data = {}
    # return render(request, "posts.html", data)
    return HttpResponse("hello")
