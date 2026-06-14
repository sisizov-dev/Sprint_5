import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import time
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def valid_user():
    email = f"sergeysizov48{random.randint(100,999)}@yandex.ru"
    name = "Серж"
    password = "123456"
    return {"name": name, "email": email, "password": password}

@pytest.fixture
def main_page(driver):
    url = "https://stellarburgers.education-services.ru/"
    driver.get(url)
    return driver



@pytest.fixture
def existing_user():
    return {
        "email": "kolya12123@yandex.ru",  # замените на реальный
        "password": "123456"           # замените на реальный
    }

