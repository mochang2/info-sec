# setting up Django to practice form based SQL injection
###### To set up, I referred to Django official documents: [Django official](https://www.djangoproject.com/)

### 0. Preparation
I assume that you already followed 01-common-step.

-----------

### 1. Check MySQL
After you create a superuser, when you do select query from sql_db.auth_user, the result would like this:  
![after create superuser](https://user-images.githubusercontent.com/63287638/120335125-2e6ffa80-c32c-11eb-9901-26c3a42a265f.PNG)
</br>
However, it's inconvenient to check the password, so I will change the password storage method to simpler one.

-----------

### 2. Change the way passwords are stored
Insert these codes into BASE_DIR/venv/Lib/site-packages/django/contrib/auth/hashers.py: 

    class PasswordStoreWithVul(BasePasswordHasher):
        algorithm = "password_with_vul"

        def salt(self):
            return ""

        def encode(self, password, salt):
            assert salt == ""
            return password[::-1]

        def decode(self, encoded):
            return {
                "algorithm": self.algorithm,
                "hash": encoded[:],
                "salt": None,
            }

        def verify(self, password, encoded):
            pass

        def safe_summary(self, encoded):
            pass

        def harden_runtime(self, password, encoded):
            pass

With this password storing way, you can simply store password in a reversed order(if you set a password as 'asdf', 'fdsa' will be stored in a database)
</br>
</br>
Then, insert this code into a 'PASSWORD_HASHERS' list under BASE_DIR/venv/Lib/site-packages/django/conf/global_settings.py:

    "django.contrib.auth.hashers.PasswordStoreWithVul",

The above code must be inserted in the first line of the list.

-----------

### 3. Create sample users
###### These users are used to practice form based SQL injection, which bypasses a normal password authentication.
Now, in an admin page(http~~locahost~~/admin), you can simply add new users not subject to hash function encryption.  
Access to the admin page, click 'Users' under AUTHENTICATION AND AUTHORIZATION, click 'ADD USER' and create sample users.  
![admin page add user button](https://user-images.githubusercontent.com/63287638/120339493-1f8b4700-c330-11eb-9e85-63a6a29c5e8f.png)
</br>
In my case, I create three users:  
![after create 3 example users](https://user-images.githubusercontent.com/63287638/120340389-f4edbe00-c330-11eb-9a36-069319855d55.PNG)
</br>
(username/password)  
exam/sqlinjection123  
exam2/formbasedinjection123  
exam3/blindinjection123  
</br>
Then, enter again

    py manage.py migrate

Your sql_db.auth_user in MySQL would be changed like this:  
![after changing password storing way](https://user-images.githubusercontent.com/63287638/120423493-7f700500-c3a5-11eb-8a71-9cf74191cf1a.PNG)
</br>

-----------

### 4. Revise login.html under users/templates/
###### Originally, to create a normal website with Django, we define the model at models.py and send queries to database through it, but we will not define the model because we will only practice SQL injection here.
Input these codes in the body part of the login.html:

    <form class="login" method="POST" enctype="application/x-www-form-urlencoded" id="login-form">
        <!-- Django requires this token before submitting post method -->
        {% csrf_token %}

        {% if user.is_authenticated %}
        <p>welcome! {{username}}</p>

        {% else %}
        <div class="login-field">
            <input type="text" class="login-input" placeholder="username" maxlength="20" name="username">
        </div>
        <div class="login-field">
            <!-- To see what I input, type is text, not password -->
            <input type="text" class="login-input" placeholder="password" name="password">
        </div>
        <button class="login-submit">
            <span class="button-text">login</span>
        </button>
        {% endif %}
    </form>

</br>

-----------

### 5. Revise the 'users' app
Change views.py of the 'users' app

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
                if user:
                    auth_login(request, user)
            except Exception as e:
                print("Unexpected input")

            data.update({"username": user.username})

        return render(request, "login.html", data)


    def logout(request):
        auth_logout(request)
        return redirect("http://127.0.0.1:8000/auth/")

Change urls.py of the 'users' app

    from django.urls import path, include
    from . import views

    app_name = "users"

    urlpatterns = [
        path("", views.login_func, name="login"),
        path("logout/", views.logout, name="logout"),
    ]

When you access to ht<span>tp://</span>localhost:port/auth/logout/, logout is executed. It makes you easier to logout.  
</br>
__Now, you are ready to practice form based sql injection.__
