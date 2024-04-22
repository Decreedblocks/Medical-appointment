from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True


class DoctorsCreate(BaseModel):
    name: str
    specialization: str
    phone: str


class DoctorsEdit(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None


doctors: dict[int, Doctors] = {
    0: Doctors(id=0, name='Dr. Yinka Wole', specialization='Gynaecology', phone='09123547585', is_available=False),
    1: Doctors(id=1, name='Dr. sylvia Edem', specialization='Optician', phone='08165075403'),
    2: Doctors(id=2, name='Dr. akproko Usman', specialization='Surgeon', phone='09034521890')

}
