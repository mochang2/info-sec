# setting up Django to practice SQL injection
###### To set up, I referred to Django official documents: [Django official](https://www.djangoproject.com/)

### 0. Preparation
Python must be installed.  
The code will be written on Visual Studio(VS).

-----------

### 1. Install a virtual environment
The reason why an independent virtual environment is needed is to prevent Python libraries downloaded from the Internet from causing conflicts. (External libraries are often dependent on each other, which can cause malfunction if the version is not correct)  
Turn on the terminal in VS and type in the working directory :

    python -m venv venv

The first venv is python module and the second venv would be the name of the virtual environment.  
</br>
These would be installed:  
![virtual env install](https://user-images.githubusercontent.com/63287638/120278132-dc10e880-c2ef-11eb-9467-dbf6cd484398.PNG)
</br>
To activate virtual environment(venv), move to(cd) ~~venv/Scripts and type .\acitvate. Then venv will be executed.

-----------

### 2. Install Django and start a project
In Scripts directory, type : 

    pip install django

When you type "pip freeze", Django==x.x.x (x.x.x means version) would be included.
</br>
Move to project's root directory, where you will start a project.
</br>
Then type in your terminal like:

    django-admin startproject ~~~

In my case, to express it has vulnerabilites, the name of the project is vulSite.
</br>
These would be installed including manage.py  
![start project](https://user-images.githubusercontent.com/63287638/120280136-4591f680-c2f2-11eb-8639-dcaacb513b76.PNG)
</br>

-----------

### 3. Install an app
An app refers to an application that performs a particular function, while a project refers to putting those apps together. Therefore, different functions are implemented by different apps.
</br>
</br>
Type in your terminal:

    py manage.py startapp app_name

These would be installed  
![startapp](https://user-images.githubusercontent.com/63287638/120281293-b8e83800-c2f3-11eb-9a57-1453c5a13ef3.PNG)
</br>
'users' app will be composed of the code related to login and it will show form based sql injection.  
'posts' app will be composed of the code related to post and it will show blind sql injection.
</br>
</br>
Open settings.py, which is in vulSite(project name) and add app names like this:  
![settings](https://user-images.githubusercontent.com/63287638/120285386-25fdcc80-c2f8-11eb-992a-fd5813d36f3f.PNG)
</br>

-----------

### 4. Create urls.py and templates directory and update views.py
Insert urls.py in vulSite(project name) directory these codes:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("auth/", include("users.urls")),
        path("posts/", include("posts.urls")),
    ]

When you type ht<span>tp://</span>localhost:portnumber/auth(or posts), you can open each app's html files(not now because there is nothing to show in apps).
</br>
</br>
Create templates directory and html files in it like this:  
![create templates](https://user-images.githubusercontent.com/63287638/120286629-6f9ae700-c2f9-11eb-8368-2dd93515e59c.PNG)
</br>
Type any texts in html files that can show this page is a login page.  
</br>
Move to views.py and add these codes:

    from django.shortcuts import render, redirect

    def login_func(request):
        data = {}
        return render(request, "login.html", data)

Create urls.py under each app and add these codes:

    from django.urls import path, include
    from . import views

    app_name = "users"

    urlpatterns = [
        path("", views.login_func, name="login"),
    ]

Add similar codes in the 'posts' app.
</br>
</br>
__When you type ht<span>tp://</span>localhost:portnumber/auth in web browser url, this page would be shown:__  
![login page ex1](https://user-images.githubusercontent.com/63287638/120288127-d8369380-c2fa-11eb-875b-0572566115e4.png)
</br>

-----------

### 5. Change database to MySQL
If you followed these steps, db.sqlite3 would be added automately. SQLite is a relatively lightweight database used by applications, not servers. I will delete db.sqlite3 and change to MySQL.  
Delete db.sqlite3. As there are no important data now, it would be okay. Then download MySQL from here: [MySQL Download](https://www.mysql.com/).  
Create a new database in MySQL with 'create database db_name', used to store users and posts like:  
![mysql new database](https://user-images.githubusercontent.com/63287638/120312660-fb217180-c313-11eb-87f3-9acc49323f58.png)
</br>
</br>
Come back to VS and type in the terminal:

    pip install mysqlclient

This module helps Django to use MySQL.
</br>
</br>
Then revise "DATABASESE" in settings.py like this:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'sql_db',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': 'MySQL well known port is 3306',
        }
    }

USER and PASSWORD are username and password of your MySQL.
</br>
</br>
From the terminal, navigate to the directory where manage.py is located(when you tried to use commands including manage.py, you should type the commands here), and enter:

    py manage.py makemigrations

and

    py manage.py migrate

When you check 'sql_db' in MySQL, these tables would be:  
![mysql first migrate](https://user-images.githubusercontent.com/63287638/120321280-17c2a700-c31e-11eb-8d16-7a94b9d4cea0.PNG)
</br>

-----------

### 6. Create a superuser
Type this where manage.py is located:

    py manage.py createsuperuser

This command makes a superuser, which has the privileges like an administrator.  
Enter the following in the terminal to reflect the changes:

    py manage.py makemigrations

and

    py manage.py migrate

Then, you can access to 'ht<span>tp://</span>localhost:port/admin' and login.  
</br>
</br>