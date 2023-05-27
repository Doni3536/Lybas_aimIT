from fastapi import *
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import *
from db import get_db
import crud
from models import dressSchema, Dress


dress_router = APIRouter()


@dress_router.post('/add-dress')
def add_dress(req: dressSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_dress(req, db)
        if result:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={'result': 'Successfully sign up'})
        else:
            return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content={'result': 'User already exists'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')

@dress_router.get('/get-dress')
def get_dress(db: Session = Depends(get_db)):
    try:
        result = crud.read_dress(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')
    