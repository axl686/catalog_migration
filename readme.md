# Создание транзакций по продуктовым каталогам

Для обновления иерархии необходимо подключить репозиторий к тестовому энву: `dev / sit` в `.private_settings.py`


## Генерация транзакции происходит через скрипт parse_doc, принимает аргументы:

- Тип каталога gaming, wim

- Вход xlsx файл

- Выход sql файл

- Проверять прилинкованные к продуктам ссылки `True\False`, необходимо, чтобы проверить доступность картинок и видео в сдн

- Стартовый и конечный номера продуктов для RogueCast


## Для генерации продуктов в RogueCast необходимо:

- Скачать последнюю версию "RogueCast Catalogue.xlsx"

- Выполнить команду, где 2 и 100 это начало и конец номера # из Excel
```shell script
python parse_doc.py /Users/AlekseiMalinovsky/Downloads/RogueCast\ Catalogue.xlsx gaming/catalog.xlsx gaming/migration.sql True 2 100
```
- Положить транзакцию `migration.sql` в репозиторий `en22-cms-service` и катануть в `dev-sit-demo-prod`

- После добавления новых продуктов, необходимо обновить иерархию (фильтры категорий)

- Выполнить:
```shell script
python build_hierarchy.py gaming gaming/hierarchy.sql
```

- Положить транзакцию `hierarchy.sql` в репозиторий `en22-cms-service` и катануть в `dev-sit-demo-prod`

- Проставить в онлайн доке `product_id / variant_id`, чтобы можно было обновлять уже занесенные продукты


## Для генерации продуктов в Wim необходимо:

- Получить продукты вим и положить например в `wim/products-wim.xlsx`

- Чтобы сгенерировать вставку новых продуктов — выполнить:
```shell script
python parse_doc.py wim wim/products-wim.xlsx wim/migration.sql True
```

- Положить транзакцию `migration.sql` в репозиторий `en22-cms-service` и катануть в `dev-sit-demo-prod`  
