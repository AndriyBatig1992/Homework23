#
# session = DBSession()
# async def search_by_name(first_name: str,
#                          db: Session) -> Optional[Contact]:
#     """To search for a record by a specific name."""
#     # return db.query(Contact).filter(Contact.name == name).first()  # .all()
#     return db.query(Contact).filter_by(first_name=first_name).first()
# async def search_contacts(par: dict, db: Session):
#     query = db.query(Contact)
#     first_name = par.get("first_name")
#     last_name = par.get("last_name")
#     email = par.get("email")
#     if first_name:
#         query = query.filter(Contact.first_name.ilike(f'%{first_name}%'))
#     if last_name:
#         query = query.filter(Contact.last_name.ilike(f'%{last_name}%'))
#     if email:
#         query = query.filter(Contact.email.ilike(f'%{email}%'))
#
#     # contacts = query.offset(par.get("skip")).limit(par.get("limit")).all()
#     contacts = query.all()
#     return contacts
# async def search_contact(db: Session, first_name: str = None,
#     last_name: str = None,
#     email: str = None,
#     favorite: bool = None
#     ):
#     contacts_query = db.query(Contact)
#
#     if first_name:
#         contacts_query = contacts_query.filter(Contact.first_name == first_name.capitalize())
#     if last_name:
#         contacts_query = contacts_query.filter(Contact.last_name == last_name.capitalize())
#     if email:
#         contacts_query = contacts_query.filter(Contact.email == email.lower())
#
#     contacts = contacts_query.all()
#
#     return contacts

#
# from src.database.db import session
# first_name="Ivan"
# email=None
# last_name="Batig"
#
#
#
# # if first_name and last_name:
# #     contacts = session.query(Contact).filter_by(Contact.first_name == first_name.capitalize(), Contact.last_name == last_name.capitalize()).all()
# if first_name and last_name:
#     contacts = session.query(Contact).filter(Contact.first_name == first_name, Contact.last_name == last_name).all()
#     print(contacts)
# if first_name:
#     contacts = session.query(Contact).filter(Contact.first_name == first_name)
# if last_name:
#     contacts = session.query(Contact).filter(Contact.last_name == last_name)
# if email:
#     contacts = session.query(Contact).filter(Contact.email == email.lower())

# for contact in contacts:
#     print(contact.last_name)


# from src.database.db import session
# par = {
#             "first_name": None,
#             "last_name": "Batig",
#             "email": None,
#             "skip": None,
#             "limit": None,
#         }
#
# query = session.query(Contact)
# print(query)
# first_name = par.get("first_name")
# last_name = par.get("last_name")
# email = par.get("email")
# if first_name:
#     query = query.filter(Contact.first_name.ilike(f'%{first_name}%'))
# if last_name:
#     query = query.filter(Contact.last_name.ilike(f'%{last_name}%'))
# if email:
#     query = query.filter(Contact.email.ilike(f'%{email}%'))
#
# contacts = query.offset(par.get("skip")).limit(par.get("limit")).all()
# print(contacts)
# for contact in contacts:
#     print(contact.first_name)
#     print(contact.last_name)



# async def search_contact(db, first_name=None, last_name=None, email=None):
#     print(first_name.capitalize())
#     contacts = None
#     if first_name and last_name:
#         contacts = db.query(Contact).filter(Contact.first_name == first_name.capitalize(), Contact.last_name == last_name.capitalize()).all()
#     if first_name:
#         contacts = db.query(Contact).filter(Contact.first_name == first_name.capitalize()).all()
#     if email:
#         contacts = db.query(Contact).filter(Contact.email == email.lower()).all()
#
#     return contacts

# class ContactResponse(ContactModel):
#     id: int = 1
#
#     class Config:
#         orm_mode = True


# @router.get("/search_by_name/{first_name}", response_model=ContactResponse, tags=['search'])
# async def search_by_name(first_name: str,
#                          db: Session = Depends(get_db)):
#     contact = await rep_contact.search_by_name(first_name, db)
#     if contact is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact Not Found")
#
#     return contact



from src.repository import contact
from src.database.db import get_db
import asyncio

# Ваша функція для тестування
# async def test_search_contacts():
#     par = {
#         "first_name": "Ivan",
#         "skip": 0,
#         "limit": 10,
#     }
#     async with get_db() as db:  # Отримайте об'єкт Session для тестування
#         contacts = await contact.search_contacts(par, db)
#         print(contacts)
#
# # Запустіть тест
#
# if __name__ == "__main__":
#     asyncio.run(test_search_contacts())




# @router.get('/search', response_model=List[ContactResponse])
# async def search_contact(
#     first_name: str = Query(None, min_length=1, max_length=25, title="Ім'я"),
#     last_name: str = Query(None, min_length=1, max_length=25, title="Прізвище"),
#     email: str = Query(None, title="Електронна пошта"),
#     db: Session = Depends(get_db)
# ):
#     contacts = await rep_contact.search_contact(db, first_name, last_name, email)
#     if not contacts:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
#     return contacts
# @router.get("/search", response_model=List[ContactResponse])
# async def search_contacts(
#         first_name: str = None,
#         last_name: str = None,
#         email: str = None,
#
#         # skip: int = Query(0, description="Number of items to skip", ge=0),
#         # limit: int = Query(10, description="Number of items to retrieve", le=100),
#         db: Session = Depends(get_db),
#
# ):
#
#     if first_name or last_name or email:
#         par = {
#             "first_name": first_name,
#             "last_name": last_name,
#             "email": email,
#             # "skip": skip,
#             # "limit": limit,
#
#         }
#         contacts = await rep_contact.search_contacts(par, db)
#     if contacts is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
#     return contacts
