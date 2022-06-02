# Patterns

This project uses 3-tiers layers as its base architecture. They include:

`/model:` domain layer

`/controller`: presentation layer

`sqlalchemy package`: is an ORM fully implements data mapper pattern. The project uses it as datasource layer.

Read more about patterns of sqlalchemy at https://techspot.zzzeek.org/2012/02/07/patterns-implemented-by-sqlalchemy/

`Repository Pattern`: sqlalchemy implemented the pattern in Session. So I refer use Session functionality anywhere. 
When interacting with database, neither use query builder nor create a new repository layer. 
Since that, we can be hands-free and focus on business logic in domain models

`Service Layer`: The project is simple enough. And the controllers are enough for controlling logic. Service layer is removed for simplifying.

# Developing Approaches

`Error Handler`: will handle exceptions and invalid form errors, and return a consistent format. Following article https://flask.palletsprojects.com/en/0.12.x/patterns/apierrors/. In my opinion, this approach will save much time in the future if developing APIs

`Code first instead of Database first`: That means the domain object should be created first, generating database schema later.
As integration tests, the db schema is generated automatically with SQLite for each running time.

`TDD`: Test cases will be made before implementing code.

# Project layout

```
.
|-- Dockerfile
|-- README.md
|-- docker-compose.yml
|-- documents
|   |-- CHECKLIST.md
|   |-- architecture.md
|   `-- setup.md
|-- flaskr
|   |-- __init__.py
|   |-- authentication.py
|   |-- commands.py
|   |-- config.py
|   |-- controller
|   |   |-- account.py
|   |   |-- book.py
|   |   `-- index.py
|   |-- database.py
|   |-- errorhandler.py
|   |-- exceptions.py
|   `-- model
|       |-- __init__.py
|       |-- book.py
|       `-- user.py
|-- requirements.txt
`-- tests
    |-- conftest.py
    |-- http_apis
    |   |-- account.http
    |   `-- book.http
    |-- integration
    |   `-- api
    |       |-- account
    |       |   |-- test_login.py
    |       |   |-- test_register.py
    |       |   `-- test_reset_password.py
    |       |-- test_base.py
    |       `-- test_books.py
    |-- unit
    |   |-- model
    |   |   `-- test_creat_new_user.py
    |   |-- test_config.py
    |   `-- test_databse.py
    `-- util.py
```



