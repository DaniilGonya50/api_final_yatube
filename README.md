# api_final
api final

Данный проект является API для сервиса публикации постов 'yatube'.
В проекте описаны эндпоинты для получения, изменения и удаления постов.

# Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```

```

```
cd yatube_api
```

Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

# Примеры запросов:

api/v1/jwt/create/ - запрос на получение токена

api/v1/posts/ GET - запрос на получение всех постов

api/v1/posts/ POST - запрос на создание поста

api/v1/posts/<post_id>/ GET - запрос на просмотр конкретного поста