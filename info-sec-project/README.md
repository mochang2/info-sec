# SQL INJECTION
###### Finding out how SQL injection is actually used and how dangerous it is.
###### I intentionally coded with vulnerability.

------------------

### Introduction
Injection was selected for OWASP TOP 1 vulnerability for 2017 and 2020, consecutively. There are many types of injection such as XML injection, XQuery injection, and so on. Among them, SQL injection is the most notorious one, so this project will address two kinds of SQL injection, form based SQL injection and blind SQL injection. Form based SQL injection is an attack that allows to perform unintended functions by entering unintended characters into the input form. Blind SQL injection is a type of SQL Injection attack that asks the database true or false questions and determines the answer based on the applications response.  
I will use Django(one of the frameworks to make web pages), which uses the Python, has a default admin page and has a default user database schema we can use with no change. Also I will use MySQL, most popular one among the database applications to show how attackers attack step by step. The ways to set up the configurations are here:
</br>
1. [common-setting](https://github.com/mochang2/info-sec/tree/master/info-sec-project/01-common-setup) &nbsp;&nbsp;&nbsp;2. [form-based-sql-injection-setting](https://github.com/mochang2/info-sec/tree/master/info-sec-project/02-form-based-sqlinjection-setup) &nbsp;&nbsp;&nbsp;3. [blind-sql-injection-setting](https://github.com/mochang2/info-sec/tree/master/info-sec-project/03-blind-sqlinjection-setup)
</br>

------------------

### Form Based SQL Injection
###### Firstly, I assume that the attackers know that the target web server uses MySQL as a database application and how views.py(Python code responsible for login processing) works.
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
The attacker can bypass authentication by arbitrarily manipulating the conditions of query statements. He or she manipulates the query statements so that the conditional clause(after where) of the query statement is always true by annotating the password-checking part via #(meaning comment in MySQL). If the conditions come after 'or' is always true(' or 2>1# etc), password authentication can be bypassed in countless ways. If the attack is successful, the attacker loges in with a user entitlement that corresponds to the first record on the returning record set. If it is an unmanaged site like the one I use in my example, it will usually be logged in as an administrator, who has almost all privileges such as reading, writing and giving permissions. Like this.  
![form based sql injection success](https://user-images.githubusercontent.com/63287638/120435926-45106300-c3b9-11eb-92a8-9321a93e5734.PNG)  
</br>

Running queries passed to the database directly from MySQL results in the following:  
![result from the mysql with '#'](https://user-images.githubusercontent.com/63287638/120437238-d2a08280-c3ba-11eb-95a6-c9a7a2f2471d.PNG)  
All of the users in the tables are returned.  
</br>

__Countermeasures for form based sql injection__  
In the case of Django, do not send queries to the database via 'raw', but rather process logins with functions such as 'authenticate' as recommended in the official document. This function essentially blocks various SQL injection.  
In addition to Django environment, there are various ways to prevent SQL injection. In APM environment, for example, there are functions in PHP language, which escape reserved special characters(#, ', " etc). Or simply, only authorized characters can be entered using a whitelist policy.  
</br>

------------------

### Blind SQL Injection
###### Again, I assume that the attackers know that the target web server uses MySQL as a database application and how views.py(Python code responsible for querying) works.
###### 'information_schema.tables' in MySQL is a default table and (column of information_schema.tables)table_type="BASE TABLE" means it is not a default table, but created by users.

Let me explain the principle first.  
![blind sql table name injection](https://user-images.githubusercontent.com/63287638/120575698-8279fc80-c45c-11eb-962c-a16c3875cbd7.PNG)  
![blind sql table name one character injection](https://user-images.githubusercontent.com/63287638/120575705-8443c000-c45c-11eb-8f53-ea8a11a5bc36.PNG)  
limit pos(ition), len(gth) : _limit_ is a function that limits the number of the results from queries. _pos_ means the starting row and _len_ means the number of rows. _pos_ starts from 0.  
substr(str(ing), pos(ition), len(gth)): _substr_ is a function that subtracts some characters from _str_ at _pos_ by _len_. _pos_ stars from 1.  
Using these functions the attackers can get the name of the tables users created and  
![blind sql column name injection](https://user-images.githubusercontent.com/63287638/120576439-b9044700-c45d-11eb-8df3-12f3c597758a.PNG)
</br>
can get the name of the columns of the tables users created. _(You may remember that the 'auth_user' table has user credentials)_  
</br>

The web page to practice blind SQL injection is a bulletin board page. When a user enters some text in the search form(placeholder is _search using title_), web server only returns the posts containing the text in the title. The below picture is the default page that basically shows all posts.  
<img src="https://user-images.githubusercontent.com/63287638/120493594-0fd63600-c3f6-11eb-8d3c-28014b82c58c.PNG" alt="https://user-images.githubusercontent.com/63287638/120493594-0fd63600-c3f6-11eb-8d3c-28014b82c58c.PNG" width="800" height="auto" />  
</br>

The function that receives text from a user and sends a query to a database is

    if request.method == "POST":
        search = request.POST.get("search", None)
        query = "select * from posts_post where title like '%%" + str(search) + "%%' order by id"
        try:
            bulletin_list = Post.objects.raw(query)
        except Exception as e:
            print("Unexpected input")
        data.update({"bulletin_list": bulletin_list})
        return render(request, "posts.html", data)

This insecure query can be emasculated by using _substr_, _limit_, _'_(open and close the string in MySQL) and _#_(comment in MySQL).  
</br>


~~ 내용을 검색 폼에 입력한다 뒤의 ~~가 참이면 모든 쿼리가 출력될 것이고 거짓이면 아무 게시도 출력이 안 될 것이다.

이를 브라우저에서 직접 이용해보겠다.

이렇게 한글자 한글자씩 알아내 db의 구조, 테이블 및 그 테이블의 컬럼 이름 등을 알 수 있다.

공격자가 최종 노가다를 통해 auth_user라는 테이블이 사용자 이름과 아이디를 저장하고 있다는 것을 알아냈다고 하자.

이를 통해 공격자는 admin 권한으로 로그인을 할 수도 있다.


이렇게 많은 노가다가 필요하므로 보통 공격자는 자동화된 툴을 이용한다.
</br>
사용자 비밀번호는 일방향 해시 알고리즘으로 저장(쉽게 알아볼 수 있는 평문 저장이 아닌)
자동화 툴로 많은 시도->로그 기록 갑작스러운 이상하게 많은 쿼리? 의심
입력값 검증, 화이트리스트+이스케이프 처리

------------------

### Conclusion
이처럼 sql injection은 인증을 우회할 수 있는 어마무시한 공격이다. 조심하는 법을 항상 익히고 취약점을 파악하려고 노력하고 보안 패치에 신경쓰자. 안 그러면 내가 힘들게 만든 웹 사이트가 닫을 수도 있다.
위에서 반복해서 얘기했지만 입력값 검증!! 젤 중요해!


#### References
<!--- span is used to prevent hyperlinks ---> 
EunHye Jung, "Django Virtualenv", ht<span>tps://</span>eunhyejung.github.io/python/2018/09/09/django-virtualenv.html  
"Django documentation", ht<span>tps://</span>www.djangoproject.com/  
"Django MySQL Interworking", ht<span>tps://</span>myjamong.tistory.com/102  
Stackoverflow, "how to get User id from auth_user table in django?", ht<span>tps://</span>stackoverflow.com/questions/15044778/how-to-get-user-id-from-auth-user-table-in-django  
박응용, "Jump to Python", ht<span>tps://</span>wikidocs.net/book/1  
"Try to use Django model", ht<span>tps://</span>dev-yakuza.posstree.com/ko/django/models/  
Stackoverflow, "escaping in Python", ht<span>tps://</span>stackoverflow.com/questions/10678229/how-can-i-selectively-escape-percent-in-python-strings  
OWASP, "blind SQL injection", ht<span>tps://</span>owasp.org/www-community/attacks/Blind_SQL_Injection  



</br></br></br></br>
이탤릭체 로 표시하려면 원하는 곳을 _, *로 감싸주면 됩니다.

볼드 처리할 곳을 __, **로 감싸주면 됩니다.

인용문은 >을 앞에 붙여주면 됩니다.

순서 없는 목록은 *, +, - 세 가지 방법을 사용할 수 있습니다. 들여쓰기를 하면 하위의 목록으로 만들 수 있습니다.