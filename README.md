# paragraph_search

 - Что нужно для запуска?   
    1) Должен быть установлен докер

    2)  ```
        paragraph_search$ docker compose up
        ```

- Примеры запросов:

    - Индексация данных 
    ```
    curl -X POST localhost:5000/indexing \
    -H "Content-Type: application/json" \
    -d '{"dataset_name_of_docs": [{"content" : "I sat on the bank of the river today."},
                                {"content" : "Я сидел у реки весь день."},
                                {"content" : "Первым в этот день дежурил Сэм, но по собственной воле к нему присоединился Арагорн. Остальные один за другим уснули. Над лощиной стремительно стала расти тишина. Ее почувствовал даже Сэм "}]}'
    ```

    - Поиск по параграфам

    ```
    curl -X POST localhost:5000/search \
    -H "Content-Type: application/json" \
    -d '{"text": "some very interesting querry", "top_k": 100}'
    ```
