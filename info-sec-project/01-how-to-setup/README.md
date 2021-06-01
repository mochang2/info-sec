# setting up Django to practice SQL injection
###### To set up, I referred to Django official documents: [Django official](https://www.djangoproject.com/)

### 0. Preparation
Python must be installed.  
The code will be written on Visual Studio(VS).

-----------

### 1. Install a virtual environment
The reason for the need for an independent virtual environment is to prevent Python libraries downloaded from the Internet from causing conflicts. (External libraries are often dependent on each other, which can cause malfunction if the version is not correct)  
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
Then type in your terminal such as:

    django-admin startproject ~~~

In my case, to express it has vulnerabilites, the name of the project is vulSite.
</br>
These would in installed including manage.py  
![start project](https://user-images.githubusercontent.com/63287638/120280136-4591f680-c2f2-11eb-8639-dcaacb513b76.PNG)
</br>


</br></br></br></br>
이탤릭체 로 표시하려면 원하는 곳을 _, *로 감싸주면 됩니다.

볼드 처리할 곳을 __, **로 감싸주면 됩니다.

인용문은 >을 앞에 붙여주면 됩니다.

순서 없는 목록은 *, +, - 세 가지 방법을 사용할 수 있습니다. 들여쓰기를 하면 하위의 목록으로 만들 수 있습니다.