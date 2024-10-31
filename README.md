# paragraph_search

 - Что нужно для запуска?   
    1) Должен быть установлен docker compose

    2)  ```
        paragraph_search$ docker compose up
        ```

- Примеры запросов:

    - Индексация данных 
    ```
    curl -X POST localhost:5000/indexing \
    -H "Content-Type: application/json" \
    -d '{
            "dataset_name_of_docs": [
                {"content" : "I sat on the bank of the river today."},
                {"content" : "In mathematics, the Riemann–Stieltjes integral is a generalization of the Riemann integral, named after Bernhard Riemann and Thomas Joannes Stieltjes"}
            ]
        }'
    ```

    - Поиск по параграфам

    ```
    curl -X POST localhost:5000/searching \
    -H "Content-Type: application/json" \
    -d '{"text": "integral", "top_k": 1}'
    ```
