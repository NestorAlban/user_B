# users_B
fastapi to create a user

- Create POST endpoint ('createuser')
- Create that receives name, email as parameters(body)
- Connect with Postgresql and creates a new record in user_test table
- Return record created

1. Run DB:
    - Run with docker
        ```shell
        docker-compose up -d db
        ```

2. Run fastapi
    - Run with uvicorn
        ```shell
        python -m uvicorn app.main:app --host localhost --reload
        ```
3. Run pytest
    ```shell
    pytest test/test_client.py -rP
    ´´´
4. commit
    - Commit with commitizen
        ```shell
        cz commit
        ´´´
