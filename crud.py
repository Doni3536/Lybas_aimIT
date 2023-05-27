from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from sqlalchemy import or_, and_
from models import Clients, clientSchema, Dressmaker, dressmakerSchema, Dress, dressSchema


# mushderileri goshmak
def client_sign_up(req, db: Session):
    user = db.query(Clients).filter(
        or_(
            Clients.name == req.name,
        )
    ).first()
    if user:
        return False
    new_add = Clients(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True

# tikincileri goshmak
def dressmaker_sign_up(req, db: Session):
    user = db.query(Dressmaker).filter(
        or_(
            Dressmaker.name == req.name,
        )
    ).first()
    if user:
        return False
    new_add = Dressmaker(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True


# koynek goshmak
def create_dress(req, db: Session):
    new_add = Dress(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add

# mushderileri gormek
def read_clients(db: Session):
    result = db.query(Clients).all()
    return result

# tikinchileri gormek
def read_dressmaker(db: Session):
    result = db.query(Dressmaker).all()
    return result


# koynekleri gormek
def read_dress(db: Session):
    result = db.query(Dress).all()
    return result

