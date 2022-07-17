from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from schemas import CarCreate
from crud import create_car, get_car_model
from database import SessionLocal


def get_date_site():
    driver = webdriver.Chrome(service=Service('chromedriver.exe'))
    db = SessionLocal()

    def get_page(address: str):
        driver.get(address)
        return BeautifulSoup(driver.page_source, "lxml")

    soup_cars = get_page("https://quto.ru/ferrari")
    cars = soup_cars.find_all('a', class_='jsx-642473951')

    for car in cars:
        url_site = "https://quto.ru"
        url_car = car['href']
        if "ferrari" not in url_car:
            continue
        soup_car = get_page(url_site + url_car)

        title = soup_car.find('h1', class_='jsx-3078905599').get_text().split()
        options = soup_car.find_all('div', {"class": ["name", "value"]})

        car = CarCreate(
            model=" ".join(title[1: len(title) - 2]),
            equipment=options[0].get_text(),
            is_available=options[1].get_text().isalnum(),
            drive=options[2].get_text(),
            power=options[3].get_text(),
            fuel=options[4].get_text(),
            consumption=options[5].get_text()
        )

        if not get_car_model(db, car.model):
            create_car(db, car)

    driver.quit()
