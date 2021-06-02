# SQL INJECTION
###### Finding out how SQL injection is actually used and how dangerous it is.

------------------

### Introduction
Injection was selected for OWASP TOP 1 vulnerability for 2017 and 2020, consecutively. There are many types of injection such as XML injection, XQuery injection, and so on. Among them, SQL injection is the most notorious one, so this project will address two kinds of SQL injection, form based SQL injection and blind SQL injection.  
I will use Django(one of the frameworks to make web pages), which uses the Python, has a default admin page and has a default user database schema we can use with no change. Also I will use MySQL, most popular one among the database applications to show how attackers attack step by step. The ways to set up the configurations are here:
</br>
1. [common-setup](https://github.com/mochang2/info-sec/tree/master/info-sec-project/01-common-setup) &nbsp;&nbsp;&nbsp;2. [form-based-sql-injection-setup](https://github.com/mochang2/info-sec/tree/master/info-sec-project/02-form-based-sqlinjection-setup) &nbsp;&nbsp;&nbsp;3. [blind-sql-injection](https://github.com/mochang2/info-sec/tree/master/info-sec-project/03-blind-sqlinjection-setup)
</br>

------------------

### Form Based SQL Injection
###### Firstly, I assume that the attackers know that the target web server uses MySQL as a database application and how views.py(Python code responsible for login processing).
Currently, the stored id, username, password in a database is:  
![after changing password storing way](https://user-images.githubusercontent.com/63287638/120423493-7f700500-c3a5-11eb-8a71-9cf74191cf1a.PNG)  
</br>
The function that processes logins at the backend is:

    def login_func(request):
        data = {}
        if request.method == "POST":
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            password = password[::-1]  # reverse the password, the way to store password in a database
            query = ("select id, username, password from auth_user where username='" + str(username) + "' and password='" + str(password) + "'")

            try:
                user = User.objects.raw(query)[0]
                if user:
                    auth_login(request, user)
            except Exception as e:
                print("Unexpected input")

            data.update({"username": user.username})

        return render(request, "login.html", data)

Find the user whose username and password matches what a user enters, and if there are multiple matching IDs, log in with the first of them.  
If login is successful, the following screen will be displayed.  
![exam login success](https://user-images.githubusercontent.com/63287638/120431184-1c856a80-c3b3-11eb-9614-7614ee99f8d2.png)  
</br>

If the user is the normal user, he or she may try logging in like this:  
![exam login trial](https://user-images.githubusercontent.com/63287638/120431179-1abba700-c3b3-11eb-8392-ea157c6e9139.png)  
</br>

However, an attacker who does not know the password can try:  
![form based sql injection trial](https://user-images.githubusercontent.com/63287638/120434696-c1a24200-c3b7-11eb-84b4-bcabc64452a4.PNG)  
The attacker can bypass authentication by arbitrarily manipulating the conditions of query statements for authentication. He or she manipulates the query statements so that the conditional clause of the query statement is always true by annotating the password-checking part via #(meaning comment in MySQL). If the attack is successful, the attacker loges in with a user entitlement that corresponds to the first record on the returning record set. If it is an unmanaged site like the one I use in my example, it will usually be logged in as an administrator, who has almost all privileges such as reading, writing and giving permissions. Like this.  
![form based sql injection success](https://user-images.githubusercontent.com/63287638/120435926-45106300-c3b9-11eb-92a8-9321a93e5734.PNG)  
</br>

Running rawquery passed to MySQL directly from MySQL results in the following results:

해결방안 : 장고 같은 경우 공식 문서에서 사용하는 authenticate 와 같은 함수로 로그인. 기본적으로 sql injection 등은 막혀 있음. 장고 외에도 APM 환경 등으로 웹서버를 만들거만 입력값 검증(허가되지 않은 특수 문자 예를 들면 db에서 예약된 특수문자들 mysql 같은 경우 #, ', " mssql같은 경우 -, ' ," 등을 이스케이프 처리함)

</br>

------------------

### Blind SQL Injection

</br>

------------------

### Conclusion

#### References
<!--- span is used to prevent hyperlinks ---> 
EunHye Jung, "Django Virtualenv", ht<span>tps://</span>eunhyejung.github.io/python/2018/09/09/django-virtualenv.html  
"Django documentation", ht<span>tps://</span>www.djangoproject.com/  
"Django MySQL Interworking", ht<span>tps://</span>myjamong.tistory.com/102  
Stackoverflow, "how to get User id from auth_user table in django?", ht<span>tps://</span>stackoverflow.com/questions/15044778/how-to-get-user-id-from-auth-user-table-in-django  
박응용, "Jump to Python", ht<span>tps://</span>wikidocs.net/book/1



00. django files
01. how to setup
02. form based sql injection(login form)
03. blind based sql injection(posts)
