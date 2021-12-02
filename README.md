# Photo-Upload

Create a frontend and backend folder


Inside frontend
1) npx create-next-app .
2) We will keep pages inside src, that is a personal choice
3) npm install --save axios




Inside Backedn folder
1) python3 -m venv venv         // It creates a virtual env with name venv
2) source venv/bin/activate     // This will activate the virtual env
3) pip install django djangorestframework psycopg2 psycopg2-binary Pillow django-cors-headers    // Installing dependencies
4) django-admin startproject image_upload .    // Start a new django app
5) python manage.py startapp image

    // register all dependencies you installed
    go to image_upload -> settings.py'
    Inside the settings.py do three things
    a) add installed apps
        # This project dependencies
        'rest_framework',
        'corsheaders',
        'image'
    b) Add middleware for cors headers
    c) add cors whitelist
    d) import os
    e) media url, media root
    f) Django permissions

6) go to image->model then create model

