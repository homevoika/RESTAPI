from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Car(Base):
    __tablename__ = "ferrari"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    equipment = Column(String)
    drive = Column(String)
    fuel = Column(String)
    power = Column(String)
    consumption = Column(String)
    is_available = Column(Boolean, default=True)


