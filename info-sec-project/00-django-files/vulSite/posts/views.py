from django.shortcuts import render, redirect
from .models import Post


def index(request):
    data = {}

    if request.method == "POST":
        pass

    bulletin_list = Post.objects.all().order_by("id")  # order all contents by id
    data.update({"bulletin_list": bulletin_list})

    return render(request, "posts.html", data)


def createposts(requests):
    Post.objects.create(title="write what you want", writer="write who you want")
    return redirect("/posts/")  # relative path
