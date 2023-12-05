from server.routes import router as ScoresAPIRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(ScoresAPIRouter)

