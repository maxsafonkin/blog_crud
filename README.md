# Blog CRUD

## Назначение

CRUD-сервис для взаимодействия с базой данных, содержащей посты блога.

## Deployment

1. Создать `.env`-файл. Пример:

    ```txt
    DB_HOST=postgres
    DB_PORT=5432
    DB_USER=user
    DB_PASSWORD=password
    DB_NAME=postgres
    ```

2. *(опционально)* Изменить переменные окружения `POSTGRES_USER` и `POSTGRES_PASSWORD` в `docker-compose.yml`

3. Указать путь до `.env`-файла в `docker-compose.yml` (изменить значение `env_file`)

4. Собрать образ и запустить контейнер

    ```bash
    docker compose up -d --build
    ```
