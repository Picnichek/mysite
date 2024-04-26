# mysite

### Локальный запуск:
* Клонировать репозиторий в локальную папку:
    ```bash
    git clone https://github.com/Picnichek/mysite.git
    cd mysite
    ```
* Создать виртуальное окружение и установить зависимости:
    windows
    ```bash
    python -m venv venv
    sourse venv/Scripts/activate
    pip install -r requirements.txt
    ```
    linux
    ```bash
    python3 -m venv venv
    Sourse venv/bin/activate
    pip install -r requirements.txt
    ```
* В папке конфигурации mysite переименовать файл ".env.template" в ".env"
* Создать базу данных PostgreSQL и заполнить ".env" в соответствии с вашими данными:
    ```bash
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=mysite # имя вашей БД
    POSTGRES_USER=postgres # пользователь
    POSTGRES_PASSWORD=postgres # пароль
    DB_HOST=127.0.0.1
    DB_PORT=5432
    ```
* Cоздание администратора и миграций, а также их применение:
    ```bash
    cd some_project
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```
* В файле "fixtures.json" уже есть тестовые данные и суперпользователь:
    - admin(пароль:admin)
    - 	test_customer(1Qaz2wsx!)
    - 	test_performer(1Qaz2wsx!)
    ```bash
        python manage.py loaddata fixtures.json
    ```
* Запускаем сервер:
    ```bash
    python manage.py runserver
    ```
