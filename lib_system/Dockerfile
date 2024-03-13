# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Копируем зависимости проекта и устанавливаем их
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копируем код проекта в контейнер
COPY . /code/

RUN python manage.py migrate