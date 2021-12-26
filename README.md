# DRF
## Lesson 1

Installation:
1. pip install django
2. django-admin startproject main .
3. pip install djangorestframework
4. pip install markdown
5. pip install django-filter
6.  python manage.py startapp authors

Making:
1. add app to settings.py
   1. rest_framework
   2. authors
2. add url to main/urls.py
   1. path('api-auth/', include('rest_framework')),
3. create model in authors/model.py
   1. class Author
4. create author/serializer.py
5. create view in author/view.py
6. makemigrations
7. migrate

## Lesson 2

Installation:
1. download mode.js from https://nodejs.org/en/ (but the best variant to install from UbuntuSoftware)
2. npx create-react-app frontend
3. in new terminal window change dir to frontend (~$ cd frontend)
4. run React as ~/Projects/GeekBrains/DRF/frontend$ npm start
5. npm install axios
6. pip install django-cors-headers
7. add info to settings.py:
   1. INSTALLED_APPS + 'corsheaders'
   2. MIDDLEWARE + 'corsheaders.middleware.CorsMiddleware'
   3. CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    ]


Making:
1. Write js code
