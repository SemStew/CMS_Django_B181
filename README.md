## CMS_Django_B181 ##

SemStew is a REST web application. It serves as a template for any restaurant, so they could customize their own web-sites based on this template.



### Starting up

1. Open terminal

2. Make sure you have installed python3.7 and higher and pip

3. Create virtual enviroment for the app:

   - `virtualenv venv`

4. Switch into the evniroment:

   - `venv\Scripts\activate`

5. Install Django and REST framework:

   - `pip install Django`
   - `pip install djangorestframework`
   - OR USE `.\setup.py install`

6. Make database tables by:

   - `python manage.py migrate`

7. Create superuser, so you can use admin part of page:

   - `python manage.py createsuperuser`
   - follow instructions
   
8. Load prepared data for database:

   - `python manage.py loaddata db.json`

