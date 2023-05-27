from pydantic import BaseModel


class clientSchema(BaseModel):
    name: str
    phone_number: str
    location: str
    bust: float 
    waist: float
    hips: float
    height: float
    weight: float

class dressmakerSchema(BaseModel):
    name: str
    phone_number: str
    location: str
    years_of_experience: float

class dressSchema(BaseModel):
    discription: str
    price: str
    location: str
    name_of_dressmaker: str
    