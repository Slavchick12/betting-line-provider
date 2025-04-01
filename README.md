# Line Provider
## Описание сервиса
Сервис предназначен для получения информации о событиях, на которые можно совершать ставки.

Документацию API доступна по адресу: http://127.0.0.1:8000/api/redoc

Swagger доступен по адресу: http://127.0.0.1:8000/api/swagger


## Информация по развертыванию проекта
##### Шаг 1. Склонируйте репозиторий на локальную машину
```bash
git clone https://github.com/Slavchick12/betting-line-provider.git
```
##### Шаг 2. Добавьте .env файл в директорию /envs/dev/.env
##### Шаг 3. Заполните .env файл опираясь на пример /envs/dev/.env.example
##### Шаг 4. Создайте сеть network "betting" для docker compose, если её не существует
```bash
docker network create betting
```
##### Шаг 5. Запустите контейнеры с предварительным билдом
```bash
docker-compose -f envs/dev/docker-compose.yml up --build
```
##### Шаг 6. Проделайте шаги для запуска второго микросервиса. Информацию по развертыванию можно найти [здесь](https://github.com/Slavchick12/betting-bet-marker/blob/main/README.md)
