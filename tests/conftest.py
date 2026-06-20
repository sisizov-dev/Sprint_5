import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

#создаёт экземпляр Chrome-драйвера
@pytest.fixture  
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

#генерирует случайные валидные данные нового пользователя
@pytest.fixture
def valid_user():
    email = f"sergeysizov48{random.randint(100,999)}@yandex.ru"
    name = "Серж"
    password = "123456"
    return {"name": name, "email": email, "password": password}

#принимает драйвер, открывает главную страницу приложения
@pytest.fixture
def main_page(driver):
    url = "https://stellarburgers.education-services.ru/"
    driver.get(url)
    return driver


#предоставляет фиксированные данные зарегистрированного пользователя
@pytest.fixture
def existing_user():
    return {
        "email": "kolya12123@yandex.ru",  
        "password": "123456"           
    }
#выполняет авторизацию
@pytest.fixture 
def authorized_main_page(main_page, existing_user):
    main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    main_page.find_element(By.XPATH, "(//input[@name='name'])").send_keys(existing_user["email"])
    main_page.find_element(By.NAME, "Пароль").send_keys(existing_user["password"])
    main_page.find_element(By.XPATH, "//button[text()='Войти']").click()
    time.sleep(2) 
    return main_page

