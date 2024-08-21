# Monolith
Description for monolith


## Architecture
1. Каждый miniapp должен решать свою бизнес логику
2. Нельзя использовать таблицы другого миниаппа, никакого шеринга данными между миниаппами
3. Отмена запроса по любой из причины должна происходить в service миниаппа с помощью кастом HTTPException
4. Кастомные HTTPException должны быть абстрактными и иметь возможность использоватся вне только одной миниаппы



## Structure
```bash
monolith 
├── alembic # Auto migrations
├── app
│   ├── miniapps # API endpoints
│   │   └── example
│   │       ├── depends.py # Depend injections
│   │       ├── models.py # Sqlalchemy table models
│   │       ├── repository.py # SQL Queries
│   │       ├── service.py # Transaction builder
│   │       ├── router.py # Define endpoints
│   │       └── shemas.py # Pydantic shemas for requests/reponses/tables
│   ├── config.py # Pydantic config load from ENV
│   ├── database.py # Database base define
│   ├── depends.py # Global dependencies
│   ├── exceptions.py # Custom exceptions
│   ├── routers.py # Api routers from miniapps
│   ├── shemas.py # Base pydantic shema
│   └── unit.py # UnitOfWork
└── main.py # Entry point
```