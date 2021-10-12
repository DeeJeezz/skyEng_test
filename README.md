# Тестовое задание для SkyEng.

## API
### GET /api/v1/resume/

##### Список всех резюме

###### Пример запроса
```
GET /api/v1/resume/
```

###### Пример ответа
```json
[
    {
        "id": "26c940a1-7228-4ea2-a3bc-e6460b172040",
        "status": "Just Watching",
        "education": "Higher",
        "owner": "admin",
        "grade": 3,
        "specialty": "Engineer",
        "salary": 70000.0,
        "experience": "*some info about experience*",
        "portfolio": "https://portfolio.com/engineer",
        "title": "Best Engineer Ever",
        "phone": "88005553535",
        "email": "engineer@example.com"
    },
    {
        "id": "e13ad0ce-c55f-4299-aa5e-f8461d237955",
        "status": "Looking For Job",
        "education": "Higher",
        "owner": "admin",
        "grade": 5,
        "specialty": "Dentist",
        "salary": 150000.0,
        "experience": "*some info about experience*",
        "portfolio": "https://portfolio.com/dentist",
        "title": "Best Dentist Ever",
        "phone": "+19095838326",
        "email": "dentist@example.com"
    },
    {
        "id": "84b08e73-6013-4f8c-ac12-9bc9659a957a",
        "status": "Not Looking",
        "education": "Secondary",
        "owner": "user",
        "grade": 2,
        "specialty": "Cook",
        "salary": 1000.0,
        "experience": "*some info about experience*",
        "portfolio": "https://portfolio.com/cook",
        "title": "Average Cook Ever",
        "phone": "+355691468542",
        "email": "cook@example.com"
    }
]
```

#### GET /api/v1/resume/\<uuid:id\>/

##### Получение резюме по id

###### Пример запроса

```
GET /api/v1/resume/26c940a1-7228-4ea2-a3bc-e6460b172040/
```

###### Пример ответа

```json
{
    "id": "26c940a1-7228-4ea2-a3bc-e6460b172040",
    "status": "Just Watching",
    "education": "Higher",
    "owner": "admin",
    "grade": 3,
    "specialty": "Engineer",
    "salary": 70000.0,
    "experience": "*some info about experience*",
    "portfolio": "https://portfolio.com/engineer",
    "title": "Best Engineer Ever",
    "phone": "88005553535",
    "email": "engineer@example.com"
}
```

#### [Protected] PATCH /api/v1/resume/\<uuid:id\>/

##### Изменение резюме. Доступно только владельцу резюме. 
##### В случае отсутствия доступа вернется 403.

###### Пример запроса

```
PATCH /api/v1/resume/26c940a1-7228-4ea2-a3bc-e6460b172040/
```
```json
{
    "id": "26c940a1-7228-4ea2-a3bc-e6460b172040",
    "status": "Just Watching",
    "education": "Higher",
    "owner": "admin",
    "grade": 3,
    "specialty": "Engineer",
    "salary": 80000.0,
    "experience": "*some info about experience*",
    "portfolio": "https://portfolio.com/engineer",
    "title": "Best Engineer Ever",
    "phone": "88005553535",
    "email": "engineer@example.com"
}
```

###### Пример ответа

```json
{
    "id": "26c940a1-7228-4ea2-a3bc-e6460b172040",
    "status": "Just Watching",
    "education": "Higher",
    "owner": "admin",
    "grade": 3,
    "specialty": "Engineer",
    "salary": 80000.0,
    "experience": "*some info about experience*",
    "portfolio": "https://portfolio.com/engineer",
    "title": "Best Engineer Ever",
    "phone": "88005553535",
    "email": "engineer@example.com"
}
```

## Запуск сервиса

```shell
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt

# Тесты
coverage run manage.py test
coverage report

python manage.py runserver
```
