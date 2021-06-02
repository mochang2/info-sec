# SQL INJECTION
###### Finding out how SQL injection is actually used and how dangerous it is.
------------------

### Introduction
Injection was selected for OWASP TOP 1 vulnerability for 2017 and 2020, consecutively. There are many types of injection such as XML injection, XQuery injection, and so on. Among them, SQL injection is the most notorious one, so this project will address two kinds of SQL injection, form based SQL injection and blind SQL injection.  
I will use Django(one of the frameworks to make web pages), which uses the Python, has a default admin page and has a default user database schema we can use with no change. Also I will use MySQL, most popular one among the database applications to show how attackers attack step by step. The ways to set up the configurations are here:
</br>
1.[common-setup](https://github.com/mochang2/info-sec/tree/master/info-sec-project/01-common-setup) 2.[form-based-sql-injection-setup](https://github.com/mochang2/info-sec/tree/master/info-sec-project/02-form-based-sqlinjection-setup) 3.[blind-sql-injection](https://github.com/mochang2/info-sec/tree/master/info-sec-project/03-blind-sqlinjection-setup)

### Form Based SQL Injection

### Blind SQL Injection

### Conclusion

#### References
<!--- span is used to prevent hyperlinks ---> 
EunHye Jung, "Django Virtualenv", ht<span>tps://</span>eunhyejung.github.io/python/2018/09/09/django-virtualenv.html  
"Django documentation", ht<span>tps://</span>www.djangoproject.com/  
"Django MySQL Interworking", ht<span>tps://</span>myjamong.tistory.com/102  
Stackoverflow, "how to get User id from auth_user table in django?", ht<span>tps://</span>stackoverflow.com/questions/15044778/how-to-get-user-id-from-auth-user-table-in-django  



00. django files
01. how to setup
02. form based sql injection(login form)
03. blind based sql injection(posts)
