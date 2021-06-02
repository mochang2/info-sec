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
                width: 400px;
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
                {{i.id}} &nbsp;&nbsp;&nbsp; {{i.title}} &nbsp;&nbsp;&nbsp; {{i.writer}} &nbsp;&nbsp;&nbsp;
                {{i.created_at}}<br>
                {% endfor %}
            </div>
            <form class="form-POST" method="POST" enctype="application/x-www-form-urlencoded">
                <!-- Django requires this token before submitting post method -->
                {% csrf_token %}

                <div class="search">
                    <input type="text" class="search-input" placeholder="search using title" maxlength="100" name="search">
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
![posts page without anything](https://user-images.githubusercontent.com/63287638/120485006-99820580-c3ee-11eb-9146-78f7b98c3d06.PNG)  
</br>

-----------

### 3. Create any dummy contents


-----------

### 4. Implement search capabilities




</br></br></br></br>
이탤릭체 로 표시하려면 원하는 곳을 _, *로 감싸주면 됩니다.

볼드 처리할 곳을 __, **로 감싸주면 됩니다.

인용문은 >을 앞에 붙여주면 됩니다.

순서 없는 목록은 *, +, - 세 가지 방법을 사용할 수 있습니다. 들여쓰기를 하면 하위의 목록으로 만들 수 있습니다.