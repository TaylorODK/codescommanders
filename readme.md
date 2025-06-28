## Тестовое задание по разработке серверного приложения

Выполнение тестового задания по разработке серверного приложения

Инструкция по локальному запуску проекта на вашем рабочем месте:

## Установка и запуск проекта

1. Клонируйте репозиторий через Git
cd <ваша директория, в которую вы хотите разместить проект>

git clone <SSH-ключ данного репозитория>

2. Создайте виртуальное окружение и активируйте его

Windows
python -m venv venv
source venv/Scripts/activate
Linux/macOS
python3 -m venv venv
source venv/bin/activate

3. Создайте файл .env в корневой папке проекта:

POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
DB_ENGINE='django.db.backends.postgresql'
SECRET_KEY='django-insecure-q&@nv(8rp$7hm&!!6hbnd*4hmcwuy356pc$*4=q(2(snfg%rzw'
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1 backend

4. Скачайте и установите Docker Desktop с официального сайта: https://www.docker.com

5. Из корневой папки выполните следующие команды:
    - cd ../infra
    - docker-compose up -d --build
    - docker compose exec backend python manage.py makemigrations api || echo "No new migrations"
    - docker compose exec backend python manage.py migrate
    - docker compose exec backend python manage.py collectstatic
    - docker compose exec backend python manage.py createsuperuser
    - docker compose exec backend cp -r /app/collected_static/. /backend_static/static/

6. Сайт будет доступен в браузере по следующей ссылке http://127.0.0.1:8000/. Подробное руководство для взаимодействия с API сервисом, прописанным внутри данного приложения, а также примеры запросов и ответов вы сможете найти по ссылке: http://127.0.0.1:8000/api/swagger/. 



