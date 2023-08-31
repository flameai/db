# Библиотека для построения микросервисов с БД

## Пример использования:


requirements.txt
```text
git+https://github.com/flameai/db.git@{tag}#common_db
```

## Линтинг кода и код-стайл:

Установка Flake8 и Black
```sh
pip install -r ./requirements_dev.txt
```
Форматирование:
```sh
black ./common
```

Проверка:
```text
flake8 ./common
```