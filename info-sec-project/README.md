# SQL INJECTION
###### Finding out how SQL injection is actually used and how dangerous it is.
------------------

### Introduction
Injection was selected for OWASP TOP 1 vulnerability for 2017 and 2020, consecutively. There are many types of injection such as XML injection, XQuery injection, and so on. Among them, SQL injection is the most notorious one, so this project will address two kinds of SQL injection, form based SQL injection and blind SQL injection.  
I will use Django(one of the frameworks to make web pages), which uses the Python, has a default admin page and has a default user database schema we can use with no change. Also I will use MySQL, most popular one among the database applications to show how attackers attack step by step. The ways to set up the configurations are here:
</br>
1. [common-setup](https://github.com/mochang2/info-sec/tree/master/info-sec-project/01-common-setup) &nbsp;&nbsp;&nbsp;2. [form-based-sql-injection-setup](https://github.com/mochang2/info-sec/tree/master/info-sec-project/02-form-based-sqlinjection-setup) &nbsp;&nbsp;&nbsp;3. [blind-sql-injection](https://github.com/mochang2/info-sec/tree/master/info-sec-project/03-blind-sqlinjection-setup)

### Form Based SQL Injection
views.py 보여주고(같은 아이디와 패스워드를 가진 경우 첫번째 아이디로 로그인됨)
공격자는 mysql을 사용한다는 것을 알고
views.py가 어떻게 동작하는지 안다고 하자
이렇게 로그인한다(패스워드 인증 무력화)
보통 db의 제일 첫번째 아이디는 관리자 아이디일 경우가 많다=>관리자 권한(웹사이트 내에서 할 수 있는 거의 모든 권한 // 읽기쓰기 유저 권한 변경 등등 거의 모든 권한)
해결방안 : 장고 같은 경우 공식 문서에서 사용하는 authenticate 와 같은 함수로 로그인. 기본적으로 sql injection 등은 막혀 있음. 장고 외에도 APM 환경 등으로 웹서버를 만들거만 입력값 검증(허가되지 않은 특수 문자 예를 들면 db에서 예약된 특수문자들 mysql 같은 경우 #, ', " mssql같은 경우 -, ' ," 등을 이스케이프 처리함)


### Blind SQL Injection

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
