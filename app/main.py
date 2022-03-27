import sys
import os

sys.path.append(os.getcwd())
import uvicorn

from app.endpoints.app import create_app

app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5001, reload=True)
