# SQL INJECTION
###### Finding out how SQL injection is actually used and how dangerous it is.
###### I intentionally coded with vulnerability.

------------------

### Introduction
Injection was selected for OWASP TOP 1 vulnerability for 2017 and 2020, consecutively. There are many types of injection such as XML injection and XQuery injection. Among them, SQL injection is the most notorious one, so this project will address two kinds of SQL injection, form based SQL injection and blind SQL injection. Form based SQL injection is an attack that allows to perform unintended queries by inserting unintended characters into the input form. Blind SQL injection is an attack that asks the database true or false questions and gets information based on the response.  
I will use Django(one of the frameworks to make web pages), which uses Python, has a default admin page and has a default _user_ database schema we can use without any changes. Also, I will use MySQL, most popular one among the database applications, to show how attackers attack step by step. The ways to set up the configurations are here:
</br>
1. [common-setting](https://github.com/mochang2/info-sec/tree/master/info-sec-project/01-common-setup) &nbsp;&nbsp;&nbsp;2. [form-based-sql-injection-setting](https://github.com/mochang2/info-sec/tree/master/info-sec-project/02-form-based-sqlinjection-setup) &nbsp;&nbsp;&nbsp;3. [blind-sql-injection-setting](https://github.com/mochang2/info-sec/tree/master/info-sec-project/03-blind-sqlinjection-setup)
</br>

------------------

### Form Based SQL Injection
###### Firstly, I assume that the attackers know that the target web server uses MySQL as a database application and how views.py(Python code responsible for login processing) works.
Currently, the stored id, username and password in the database are:  
![after changing password storing way](https://user-images.githubusercontent.com/63287638/120423493-7f700500-c3a5-11eb-8a71-9cf74191cf1a.PNG)  
</br>
The function that processes logins at the backend is:

    def login_func(request):
        data = {}
        if request.method == "POST":
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            password = password[::-1]  # reverse the password, the way to store password in a database
            query = "select id, username, password from auth_user where username='" + str(username) + "' and password='" + str(password) + "'"

            try:
                user = User.objects.raw(query)[0]
                if user:
                    auth_login(request, user)
            except Exception as e:
                print("Unexpected input")

            data.update({"username": user.username})

        return render(request, "login.html", data)

This function finds the user whose username and password matches what a client enters, and if there are multiple results, the client logs in with the first of them.  
If login is successful, the following screen will be displayed.  
![exam login success](https://user-images.githubusercontent.com/63287638/120431184-1c856a80-c3b3-11eb-9614-7614ee99f8d2.png)  
</br>

If the client is a normal client, he or she may try logging in like this:  
![exam login trial](https://user-images.githubusercontent.com/63287638/120431179-1abba700-c3b3-11eb-8392-ea157c6e9139.png)  
</br>

However, attackers who do not know the password can try:  
![form based sql injection trial](https://user-images.githubusercontent.com/63287638/120434696-c1a24200-c3b7-11eb-84b4-bcabc64452a4.PNG)  
The attackers can bypass authentication by arbitrarily manipulating the conditions of query statements. He or she manipulates the query statements so that the conditional clause(after _where_) of the query statement is always true by annotating the password-checking part via #(meaning comment in MySQL). If the conditions come after _or_ is always true(' or 2>1# etc), password authentication can be bypassed in countless ways. If the attack is successful, the attackers log in with entitlement that corresponds to the first record on the returning record set. If it is an unmanaged site like the one I use in my example, it will usually be logged in as an administrator, who has almost all privileges such as reading, writing and giving permissions. Like this.  
![form based sql injection success](https://user-images.githubusercontent.com/63287638/120435926-45106300-c3b9-11eb-92a8-9321a93e5734.PNG)  
</br>

I'll run it directly in MySQL and compare the results.  
![form based sql injection in MySQL](https://user-images.githubusercontent.com/63287638/120585689-308da280-c46d-11eb-8873-08761bc82cf6.PNG)
The first result is from a normal client whose username is exam while the second result is from an attacker who manipulates a query. 
As the clause after _#_, password validation part in the second query, has no meaning, all of the users in the tables are returned.  
</br>

------------------

### Blind SQL Injection
###### Again, I assume that the attackers know that the target web server uses MySQL as a database application and how views.py(Python code responsible for querying) works.
###### _information_schema.tables_ in MySQL is a default table and (column of information_schema.tables)_table_type="BASE TABLE"_ means it is not a default table, but created.

Let me explain the principle first.  
![blind sql table name injection](https://user-images.githubusercontent.com/63287638/120575698-8279fc80-c45c-11eb-962c-a16c3875cbd7.PNG)  
![blind sql table name one character injection](https://user-images.githubusercontent.com/63287638/120575705-8443c000-c45c-11eb-8f53-ea8a11a5bc36.PNG)  
limit pos(ition), len(gth) : _limit_ is a function that limits the number of the results from queries. _pos_ means the starting row and _len_ means the number of rows. _pos_ starts from 0.  
substr(str(ing), pos(ition), len(gth)): _substr_ is a function that subtracts some characters from _str_ at _pos_ by _len_. _pos_ stars from 1.  
</br>

Using these functions, the attackers can get the name of the tables which an administrator created and  
![blind sql column name injection](https://user-images.githubusercontent.com/63287638/120576439-b9044700-c45d-11eb-8df3-12f3c597758a.PNG)
</br>
can get the name of the columns of the tables. _(You may remember that the 'auth_user' table has user credentials)_  
</br>

The web page to practice blind SQL injection is a bulletin board page. When a client enters some text in the search form(placeholder is _search using title_), web server only returns the posts containing the text in the title. The below picture is the default page that basically shows all posts.  
<img src="https://user-images.githubusercontent.com/63287638/120493594-0fd63600-c3f6-11eb-8d3c-28014b82c58c.PNG" alt="https://user-images.githubusercontent.com/63287638/120493594-0fd63600-c3f6-11eb-8d3c-28014b82c58c.PNG" width="800" height="auto" />  
</br>

The function that receives text from a client and sends a query to a database is

    if request.method == "POST":
        search = request.POST.get("search", None)
        query = "select * from posts_post where title like '%%" + str(search) + "%%' order by id"
        try:
            bulletin_list = Post.objects.raw(query)
        except Exception as e:
            print("Unexpected input")
        data.update({"bulletin_list": bulletin_list})
        return render(request, "posts.html", data)

This insecure _query_ can be abused using _substr_, _limit_, _'_(open and close the string in MySQL) and _#_(comment in MySQL).  
</br>

Attackers enter
>' and substr((select table_name from information_schema.tables where table_type="BASE TABLE" limit 185,1),1,1)='a'#

If the first character of 186th BASE TABLE is 'a', all of the posts will be returned. However, if the first character of 186th BASE TABLE is not 'a', none of the posts will be returned. _(As 186th BASE TABLE is a 'auth_user' table in my MySQL, all of the posts are printed)_.  
<img src="https://user-images.githubusercontent.com/63287638/120581668-26b47100-c466-11eb-8734-1f354175f0e2.PNG" alt="https://user-images.githubusercontent.com/63287638/120581668-26b47100-c466-11eb-8734-1f354175f0e2.PNG" width="800" height="auto" />  
</br>

If attackers enter('a' is chaged to 'b')
>' and substr((select table_name from information_schema.tables where table_type="BASE TABLE" limit 185,1),1,1)='a'#

Nothing is returned.  
<img src="https://user-images.githubusercontent.com/63287638/120581870-7f840980-c466-11eb-86a2-164fd484e8d1.PNG" alt="https://user-images.githubusercontent.com/63287638/120581870-7f840980-c466-11eb-86a2-164fd484e8d1.PNG" width="800" height="auto" />  
</br>

Since the way of figuring out one letter is slow and needs many efforts, attackers usually use automated tools. Through the blind SQL injection attack, attackers can know the schema of the database, the name of the tables and the name of the columns of the tables. 
</br>

Running queries passed to the database directly from MySQL results in the following(same result with the above picture):  
![result from the mysql - blind sql injection](https://user-images.githubusercontent.com/63287638/120587774-f58d6e00-c470-11eb-8da2-5af4cbe3d3c1.PNG)
</br>
</br>

Now, let's assume one attacker, with many trials, eventually knows that there is an 'auth_user' table that has user credentials and the name of the columns of the table. With _union select_, the attacker can know the id, username and password of the users. The attacker enters  
>' and 1=2 union select id, username, password, null from auth_user#

Any false condition follows after _and_ for the backend function to return nothing from a 'posts_post' table. As a result, only user credentials are returned.  
![blind sql the end result - get credentials](https://user-images.githubusercontent.com/63287638/120583324-f28e7f80-c468-11eb-84bf-5d26b56e50c4.PNG)  
With this information, the attacker can log in as an __administrator__.  
</br>

------------------

### Conclusion
As you have seen, SQL injection can attack the database that typically contains all the interesting and critical data for applications. This is why SQL injection is a common attack. If this vulnerability is not defended well, the web server will be no different from the simple text. Therefore, we should always try to prevent vulnerability from threats, and if security patches are made, we should make a habit of checking them carefully.  

__Countermeasures for SQL injection__  
The best way to prevent SQL injection is to check input values. Checking inputs at frontend can be detoured easily using web proxy tools, so doing at backend is necessary. A whitelist policy that denotes allowed special characters is recommended, not a blacklist policy.  
Also, use secure functions. In the case of Django, do not send queries to the database via _raw_, but rather send queries with functions recommended in the official document. They essentially blocks various SQL injection. In addition to Django environment, there are ways to prevent SQL injection in various envionments. In APM environment, for example, there are functions in PHP language such as _htmlspecialchars_, which escape reserved special characters(#, ', " etc).  
Other ways to prevent SQL injection, according to OWASP, is to use prepared statments or stored procedures. Giving least privileges to accounts which run the web server to prevent falsification of the database is another good countermeasure.  
</br>

------------------

#### References
<!--- span is used to prevent hyperlinks ---> 
EunHye Jung, "Django Virtualenv", ht<span>tps://</span>eunhyejung.github.io/python/2018/09/09/django-virtualenv.html  
"Django documentation", ht<span>tps://ww</span>w.djangoproject.com/  
"Django MySQL Interworking", ht<span>tps://</span>myjamong.tistory.com/102  
Stackoverflow, "how to get User id from auth_user table in django?", ht<span>tps://</span>stackoverflow.com/questions/15044778/how-to-get-user-id-from-auth-user-table-in-django  
박응용, "Jump to Python", ht<span>tps://</span>wikidocs.net/book/1  
"Try to use Django model", ht<span>tps://</span>dev-yakuza.posstree.com/ko/django/models/  
Stackoverflow, "escaping in Python", ht<span>tps://</span>stackoverflow.com/questions/10678229/how-can-i-selectively-escape-percent-in-python-strings  
OWASP, "blind SQL injection", ht<span>tps://</span>owasp.org/www-community/attacks/Blind_SQL_Injection  
PHP official document, "htmlspcialchars", ht<span>tps://ww</span>w.php.net/manual/en/function.htmlspecialchars.php  
OWASP, "SQL Injection Prevention Cheat Sheet", ht<span>tps://</span>cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
