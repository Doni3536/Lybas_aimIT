from sqlalchemy import *
from sqlalchemy.orm import *
from db import Base
from datetime import *


class Clients(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    location = Column(String)
    bust = Column(Float)
    waist = Column(Float)
    hips = Column(Float)
    height = Column(Float)
    weight = Column(Float)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    
class Dressmaker(Base):
    __tablename__ = 'dressmaker'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    location = Column(String)
    years_of_experience = Column(Float)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    

class Dress(Base):
    __tablename__ = 'dress'
    id = Column(Integer, primary_key=True, index=True)
    discription = Column(String)
    price = Column(String)
    location = Column(String)
    name_of_dressmaker = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)