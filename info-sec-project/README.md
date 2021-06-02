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

            data.update({"username": username})

        return render(request, "login.html", data)

Find the user whose username and password you entered match, and if there are multiple matching IDs, log in with the first of them.  
If login is successful, the following screen will be displayed.  
![exam login success](https://user-images.githubusercontent.com/63287638/120430744-7174b100-c3b2-11eb-981c-34fb05a63dba.PNG)  
</br>

If the user is the normal user, he or she may try like this:  
![exam login trial](https://user-images.githubusercontent.com/63287638/120430743-6faaed80-c3b2-11eb-816d-ac5ab5131245.PNG)  
</br>


이렇게 로그인한다(패스워드 인증 무력화)
보통 db의 제일 첫번째 아이디는 관리자 아이디일 경우가 많다=>관리자 권한(웹사이트 내에서 할 수 있는 거의 모든 권한 // 읽기쓰기 유저 권한 변경 등등 거의 모든 권한)
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
