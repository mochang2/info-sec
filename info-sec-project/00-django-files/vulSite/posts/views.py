from django.shortcuts import render, redirect
from .models import Post


def index(request):
    data = {}

    if request.method == "POST":
        search = request.POST.get("search", None)
        query = (
            "select * from posts_post where title like '%%"
            + str(search)
            + "%%' order by id"
        )
        try:
            bulletin_list = Post.objects.raw(query)
        except Exception as e:
            print("Unexpected input")
        data.update({"bulletin_list": bulletin_list})
        return render(request, "posts.html", data)

    bulletin_list = Post.objects.all().order_by("id")  # order all contents by id
    data.update({"bulletin_list": bulletin_list})

    return render(request, "posts.html", data)


def createposts(requests):
    Post.objects.create(title="write what you want", writer="write who you want")
    return redirect("/posts/")  # relative path
