# Django ORM Project

## Задача 1: Школа
Изменение связи ForeignKey → ManyToManyField между Student и Teacher.

## Задача 2: Статьи и теги
Реализация связи многие-ко-многим с промежуточной моделью и валидацией основного тега.

## Установка
1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py loaddata school.json` (для задачи 1)
4. `python manage.py loaddata articles.json` (для задачи 2)
5. `python manage.py runserver`
