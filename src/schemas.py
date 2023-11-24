from datetime import datetime, date
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Union


class ContactModel(BaseModel):
    first_name: str = Field(default=" ", examples=["Ivan", "Oleg"], min_length=1, max_length=25, title="Ім'я")
    last_name: str = Field(default=" ", examples=["Batig", "Djus"], min_length=1, max_length=25, title="Прізвище")
    email: EmailStr
    phone: Union[str, None] = Field(None, examples=["+380 44 123-4567", "+380 (44) 1234567", "+380441234567"], max_length=25, title="Номер телефону")
    birthday: Optional[date] = None
    comments: Union[str, None] = Field(default=None, title="Додаткові дані")
    favorite: bool = False


class ContactFavoriteModel(BaseModel):
    favorite: bool = False



class ContactResponse(BaseModel):
    id: int
    first_name: Union[str, None]
    last_name: Union[str, None]
    email: Union[EmailStr, None]
    phone: Union[str, None]
    birthday: Union[date, None]
    comments: Union[str, None]
    favorite: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


