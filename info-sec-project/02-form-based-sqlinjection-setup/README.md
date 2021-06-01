# setting up Django to practice SQL injection
###### To set up, I referred to Django official documents: [Django official](https://www.djangoproject.com/)

### 0. Preparation
I assume that you already followed 01-common-step.

-----------

### 1. Check MySQL
After you create a superuser, when you do select query from sql_db.auth_user, the result would like this:  
![after create superuser](https://user-images.githubusercontent.com/63287638/120335125-2e6ffa80-c32c-11eb-9901-26c3a42a265f.PNG)
</br>
However, it's inconvenient to check the password, so I'll change the password storage method simply.

-----------

### 2. Change the way passwords are stored
Insert these codes into BASE_DIR/venv/Lib/site-packages/django/contrib/auth/hashers.py: 

    class PasswordStoreWithVul(BasePasswordHasher):
        algorithm = "password_with_vul"

        def salt(self):
            return ""

        def encode(self, password, salt):
            assert salt == ""
            return password[::-1]

        def decode(self, encoded):
            return {
                "algorithm": self.algorithm,
                "hash": encoded[:],
                "salt": None,
            }

        def verify(self, password, encoded):
            pass

        def safe_summary(self, encoded):
            pass

        def harden_runtime(self, password, encoded):
            pass

Then, insert this code into a 'PASSWORD_HASHERS' list under BASE_DIR/venv/Lib/site-packages/django/conf/global_settings.py:

    "django.contrib.auth.hashers.PasswordStoreWithVul",

The above code must be inserted in the first line of the list.

-----------

### 3. Create sample users
###### These users are used to practice form based SQL injection, which bypasses a normal password authentication.

exam/sqlinjection123
exam2/formbasedinjection123
exam3/blindinjection123

</br></br></br></br>

todo: mysql 연동 -> 슈퍼유저 만들기 -> admin 사이트 가서 아이디 몇 개 더 만들고 mysql과 연동이 되었는지 확인 -> 로그인폼 만들기 -> sql injection 시도


</br></br></br></br>
이탤릭체 로 표시하려면 원하는 곳을 _, *로 감싸주면 됩니다.

볼드 처리할 곳을 __, **로 감싸주면 됩니다.

인용문은 >을 앞에 붙여주면 됩니다.

순서 없는 목록은 *, +, - 세 가지 방법을 사용할 수 있습니다. 들여쓰기를 하면 하위의 목록으로 만들 수 있습니다.