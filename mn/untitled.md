1.Django Project 생성

django-admin startproject 프로젝트 명

2.APP 생성

python manage.py startapp App_name

3.APP 등록

#settings.py

INSTALLED_APP = {
    'app_name'
}

4.MTV 패턴
- URL -> Pattern 작성 (path, include)
- Model -> Class 작성 (Models.Model)
- View -> 웹 요청 응답 로직 작성 (views.py) GET, POST
- Templates -> 각각 액ㅂ에 templates/app_name/xx.html

5.서버 실행

python manage.py runserver

6.모델 작업

1) models.py 파일을 작성했으면
2) python manage.py makemigrations [app_name]
3) python manage.py migrate
4) python manage.py showmigrations

7.Admin
