from typing import Optional
from pydantic import BaseModel


class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


class PatientsCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


class PatientsEdit(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    phone: Optional[str] = None


patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='Lex Udo', age=30, sex='male', weight=109.5, height=75.5, phone='08024564568'
    ),
    1: Patients(
        id=1, name='okuku Nelson', age=20, sex='male', weight=90.5, height=72.5, phone='08034532179'
    ),
    2: Patients(
        id=2, name='Benjamin Ekpatt', age=10, sex='female', weight=86, height=79, phone='08126679054'
    )
}
