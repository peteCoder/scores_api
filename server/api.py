
from server.routes import router as ScoresAPI
from fastapi import FastAPI

app = FastAPI()

app.include_router(ScoresAPI)

