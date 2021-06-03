# setting up Django to practice blind SQL injection
###### To set up, I referred to Django official documents: [Django official](https://www.djangoproject.com/)

### 0. Preparation
I assume that you already followed 01-common-step.

-----------

### 1. Define a model and applying changes to databases
Insert these codes into models.py under the 'posts' app

    class Post(models.Model):
        # id : auto created field
        title = models.CharField(max_length=100)
        writer = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

Insert thes codes into admin.py under the 'posts' app

    from .models import Post

    admin.site.register(Post)

To apply changes in models, type 'py manage.py makemigrations posts(:app name)' and 'py manage.py migrate posts(:app name)'  
![makemigrations and migrate after creating Post model](https://user-images.githubusercontent.com/63287638/120483630-4196cf00-c3ed-11eb-90b4-5935d3ac34a5.png)  
</br>

When you see MySQL again, changes would be applied.  
![mysql new table-posts](https://user-images.githubusercontent.com/63287638/120484004-9b979480-c3ed-11eb-82f6-90f33264daf8.PNG)
</br>
There will be nothing in posts_post table now.  

-----------

### 2. Revise posts.html and views.py
Delete unnecessary codes and insert these codes into posts.html:

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <!-- screen -->
        <meta name="viewpoint" content="width=device-width, initial-scale=1">
        <title>bulletin board</title>

        <style>
            html, body {
                height: 100%;
                overflow: auto;
            }
            body {
                margin: 0;
                margin-top: 100px;
            }
            .wrapper {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .bulletin-title {
                font-size: 84px;
                font-weight: bolder;
            }
            .header {
                display: flex;
                width: 700px;
                justify-content: space-between;
            }
            .bold {
                font-weight: bold;
            }
            input {
                border: 1px solid black;
                width: 720px;
                height: 23.6px;
            }
            .form-POST {
                display: flex;
                justify-items: center;
            }
        </style>
    </head>

    <body>
        <div class="wrapper">
            <div class="bulletin-title">BULLETIN BOARD</div>
            <div class="header">
                <span class="bold">Num</span>
                <span class="bold">Title</span>
                <span class="bold">Writer</span>
                <span class="bold">Created</span>
            </div>
            <div class="bulletins">
                {% for i in bulletin_list %}
                {{i.id}} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {{i.title}}
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {{i.writer}}
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {{i.created_at}}<br>
                {% endfor %}
            </div>
            <form class="form-POST" method="POST" enctype="application/x-www-form-urlencoded">
                <!-- Django requires this token before submitting post method -->
                {% csrf_token %}

                <div class="search">
                    <input type="text" class="search-input" placeholder="search using title" maxlength="200" name="search">
                </div>
                <button class="search-submit">
                    <span class="button-text">OK</span>
                </button>
            </form>
        </div>
        </div>
    </body>

    </html>

Revise views.py under the 'posts' app like this:

    from django.shortcuts import render, redirect
    from .models import Post

    def index(request):
        data = {}

        if request.method == "POST":
            pass

        bulletin_list = Post.objects.all().order_by("id")  # order all contents by id
        data.update({"bulletin_list": bulletin_list})

        return render(request, "posts.html", data)

</br>
If you access to ht<span>tp://</span>localhost:port/posts/, the web server will give this page as a response.</br>
<img src="https://user-images.githubusercontent.com/63287638/120486142-b5d27200-c3ef-11eb-9fea-0089cce39e65.PNG" alt="https://user-images.githubusercontent.com/63287638/120486142-b5d27200-c3ef-11eb-9fea-0089cce39e65.PNG" width="800" height="auto" />  

-----------

### 3. Create any dummy contents
I will not implement detailed functions and will simply create fake posts through url access.  
Add these codes on views.py under the 'posts' app:

    def createposts(requests):
        Post.objects.create(title="write what you want", writer="write who you want")
        return redirect("/posts/")  # relative path

Write the title you want to write where 'write what you want' is and write the writer you want to write where 'write who you want' is.  
Also, add these codes on urlpatterns of urls.py under the 'posts' app:

    path("createposts/", views.createposts, name="createposts"),

When you access to ht<span>tp://</span>localhost:port/posts/createposts/, a new fake writing will be posted. If you try several times, the web server will respond like this screen:  
<img src="https://user-images.githubusercontent.com/63287638/120493594-0fd63600-c3f6-11eb-8d3c-28014b82c58c.PNG" alt="https://user-images.githubusercontent.com/63287638/120493594-0fd63600-c3f6-11eb-8d3c-28014b82c58c.PNG" width="800" height="auto" />
</br>

It is also added to MySQL.  
![mysql new table-posts with dummy contents](https://user-images.githubusercontent.com/63287638/120494259-a4409880-c3f6-11eb-8241-e3c8e5b2ab3e.PNG)
</br>

-----------

### 4. Implement search capabilities
Revised the function index in views.py under the 'posts' app, where I have wrapped up roughly(if ~~~: pass).

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

When you type something in the search input box, the result will be returned.
__Now, you are ready to practice form based sql injection.__
</br>
