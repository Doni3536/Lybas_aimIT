from fastapi import *
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import *
from db import get_db
import crud
from models import dressmakerSchema, Dressmaker



dressmaker_router = APIRouter()


@dressmaker_router.post('/add-dressmaker')
def add_dressmaker(req: dressmakerSchema, db: Session = Depends(get_db)):
    try:
        result = crud.dressmaker_sign_up(req, db)
        if result:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={'result': 'Successfully sign up'})
        else:
            return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content={'result': 'User already exists'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')

@dressmaker_router.get('/get-dressmaker')
def get_dressmaker(db: Session = Depends(get_db)):
    try:
        result = crud.read_dressmaker(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')
    