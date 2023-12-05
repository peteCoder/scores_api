
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/", tags=["Root"])
async def read_root():
  return { 
        "message": "Welcome to my football scores api application, use the /docs route to proceed"
    }


@router.get("/scores", tags=["Root"])
async def score_root():
  return { 
        "message": "Hello scores"
    }


