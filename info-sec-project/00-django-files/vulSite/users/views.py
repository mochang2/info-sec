from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


def login_func(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        password = password[::-1]  # reverse the password
        query = (
            "select id, username, password from auth_user where username='"
            + str(username)
            + "' and password='"
            + str(password)
            + "'"
        )

        try:
            user = User.objects.raw(query)[0]
            # print(user.id)
            if user:
                auth_login(request, user)
        except Exception as e:
            # print(e)
            print("Unexpected input")

        data.update({"username": username})

    return render(request, "login.html", data)


def logout(request):
    auth_logout(request)
    return redirect("http://127.0.0.1:8000/auth/")
