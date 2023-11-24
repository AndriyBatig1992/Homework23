from datetime import date, timedelta
from sqlalchemy.orm import Session
from src.schemas import ContactModel
from src.database.models import Contact
from typing import Optional, Union

async def get_contacts(db: Session, skip: int, limit: int, favorite: Union[bool, None]=None):
    query = db.query(Contact)
    if favorite is not None:
        query =query.filter_by(favorite=favorite)
    contact = query.offset(skip).limit(limit).all()
    return contact


async def get_contact_by_id(contact_id: int, db:Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact



async def get_contact_by_email(email: str, db:Session):
    contact = db.query(Contact).filter_by(email=email).first()
    return contact


async def create(body: ContactModel, db:Session):
    contact = Contact(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        phone=body.phone,
        birthday=body.birthday,
        comments=body.comments,
        favorite=body.favorite,
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update(contact_id: int, body:ContactModel, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.comments = body.comments
        contact.favorite = body.favorite
        db.commit()
    return contact



async def favorite_update(contact_id: int, body: ContactModel, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.favorite = body.favorite
        db.commit()
    return contact


async def delete(contact_id, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact



async def search_contacts(par: dict, db: Session):
    query = db.query(Contact)
    first_name = par.get("first_name")
    last_name = par.get("last_name")
    email = par.get("email")
    if first_name:
        query = query.filter(Contact.first_name.ilike(f'%{first_name}%'))
    if last_name:
        query = query.filter(Contact.last_name.ilike(f'%{last_name}%'))
    if email:
        query = query.filter(Contact.email.ilile(f'%{email}%'))

    contact = query.offset(par.get("skip")).limit(par.get("limit"))
    return contact



async def search_birthday(par:dict, db: Session):
    days_param = par.get("days", 7)
    days = int(days_param)
    days += 1
    filter_after = date.today()
    filter_before = date.today() + timedelta(days=days)
    query = db.query(Contact)
    query = query.filter(Contact.birthday > filter_after, Contact.birthday <= filter_before)
    contacts = query.offset(par.get("skip")).limit(par.get("limit"))
    return contacts