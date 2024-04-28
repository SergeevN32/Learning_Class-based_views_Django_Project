# Form Project

Тестовое приложение, отображающее набор форм, отправляющих различные типы данных в БД, созданное для ознакомления с Django Class-based views.

## Quickstart

Run the following commands to bootstrap your environment:
    
    pip install virtualenv
    git clone https://github.com/niksergs/Learning_Class-based_views_Django_Project
    cd form_project

    python -m venv venv
    venv/Scripts/activate.bat
    pip install -r requirements.txt

Run the app locally:

    python manage.py runserver 0.0.0.0:8000

Run the app with gunicorn:

    pip install gunicorn
    gunicorn form_project.wsgi:application -b 0.0.0.0:8000
