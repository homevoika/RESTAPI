from sqlalchemy.orm import Session
import models
import schemas


def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()


def get_car_model(db: Session, car_model: str):
    return db.query(models.Car).filter(models.Car.model == car_model).first()


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Car).offset(skip).limit(limit).all()


def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(
        model=car.model,
        equipment=car.equipment,
        drive=car.drive,
        fuel=car.fuel,
        power=car.power,
        consumption=car.consumption,
        is_available=car.is_available
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def delete_car(db: Session, car_id: int):
    db.query(models.Car).filter(models.Car.id == car_id).delete()
    db.commit()


def update_car(db: Session, car_id: int, car: schemas.CarCreate):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    db_car.model = car.model
    db_car.equipment = car.equipment
    db_car.drive = car.drive
    db_car.fuel = car.fuel
    db_car.power = car.power
    db_car.consumption = car.consumption
    db_car.is_available = car.is_available
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car