from pydantic import BaseModel


class CarBase(BaseModel):
    model: str
    equipment: str
    drive: str = None
    fuel: str = None
    power: str = None
    consumption: str = None
    is_available: bool


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int

    class Config:
        orm_mode = True