Проект домашней библиотеки. 

Запуск локального сервера:

Распакуйте проект в папку с:\my_site
Откройте командную строку и зайдите в директорию проекта:
cd c:\my_site

Создате виртуальное окружение:
python -m venv django

Активируйте виртуальное окружение:
django\Scripts\activate.bat

Установите все необходимые пакеты:
pip install -r requirements.txt

Запустите локальный сервер:
python manage.py runserver