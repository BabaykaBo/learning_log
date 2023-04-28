# Learning Log
This is my first Django project. It is the Django-based web application for the records entry.

## Dependencies:
* asgiref==3.5.2
* beautifulsoup4==4.11.1
* dj-database-url==1.2.0
* Django==4.1.4
* django-bootstrap4==22.3
* django-heroku==0.3.1
* gunicorn==20.1.0
* psycopg2==2.9.5
* soupsieve==2.3.2.post1
* sqlparse==0.4.3
* tzdata==2022.7
* whitenoise==6.2.0

You can install these using ***pip install -r requirements.txt***
P.S. Some dependencies are required for using PostgreSql and Heroku deployment. So, if you use another database or deployment platform, Some dependencies may be not actual.

## Running:
### Manually
After cloning this repo, create the database: ***python3 manage.py migrate***
And then create admin account by running: ***python3 manage.py createsuperuser***
Then you should be able to run the server.

## Features:
### User system
* register new user
* login exicting user
* logout

### Topics
* user can create new topics
* user can watch list of his topics and the specific topic with its entries
* user can create new entries for the specific topic and edit them
