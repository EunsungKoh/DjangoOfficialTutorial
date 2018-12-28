# Django Tutorial
> https://docs.djangoproject.com/ko/1.11/intro/

> - Usage :
>	- python manage.py nserver 7070
>	- http://127.0.0.1:7070/polls/
>	- http://127.0.0.1:7070/admin/
>		- admin
>		- 123qwe123
- This code is made by Eunsung Koh.
- Env
	- Linux, Ubuntu 18.04.1 LTS
	- python 3.6.7
	- But, This code is following 1.11 version of official Django's documentation by mistake.

- Usage:
	- $ ~/officialDocumentation/mysite# python3.6 -m venv env
	- $ ~/officialDocumentation/mysite# source env/bin/activate
	- $ pip install django==1.11.0
	- $ /officialDocumentation/mysite# python manage.py runserver

- tree of the code
```
tree ./
./
├── mysite
│   ├── db.sqlite3
│   ├── manage.py
│   ├── mysite
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── settings.py
│   │   ├── settings.pyc
│   │   ├── urls.py
│   │   ├── urls.pyc
│   │   ├── wsgi.py
│   │   └── wsgi.pyc
│   └── polls
│       ├── admin.py
│       ├── admin.pyc
│       ├── apps.py
│       ├── apps.pyc
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   ├── 0001_initial.pyc
│       │   ├── 0002_auto_20181220_1643.py
│       │   ├── 0002_auto_20181220_1643.pyc
│       │   ├── __init__.py
│       │   └── __init__.pyc
│       ├── models.py
│       ├── models.pyc
│       ├── templates
│       │   └── polls
│       │       ├── detail.html
│       │       ├── index.html
│       │       └── results.html
│       ├── tests.py
│       ├── urls.py
│       ├── urls.pyc
│       ├── views.py
│       └── views.pyc
└── Readme.MD
```
