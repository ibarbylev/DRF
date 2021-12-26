# DRF

installation:
1. pip install django
2. django-admin startproject main .
3. pip install djangorestframework
4. pip install markdown
5. pip install django-filter
6.  python manage.py startapp authors

making:
1. add app to settings.py
   1. rest_framework
   2. authors
2. add url to main/urls.py
   1. path('api-auth/', include('rest_framework')),
3. create model in authors/model.py
   1. class Author
4. create author/serializer.py
5. create view in author/view.py