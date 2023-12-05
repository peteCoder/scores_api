import uvicorn
from dotenv import dotenv_values
from server.api import app

config = dotenv_values(".env")


if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


