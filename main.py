import uvicorn
from dotenv import dotenv_values

config = dotenv_values(".env")

PORT = int(config["PORT"])


if __name__ == "__main__":
  uvicorn.run("server.api:app", host="127.0.0.1", port=8000, reload=True)


