import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators 

class TestConstructor:
    def test_click_constructor(self, authorized_main_page):  # проверяем переход по кнопке конструктор
        authorized_main_page.find_element(*ConstructorLocators.PERSONAL_ACCOUNT_LINK).click()   # нажимаем кнопку личный кабинет
        authorized_main_page.find_element(*ConstructorLocators.CONSTRUCTOR_LINK).click()        # нажимаем кнопку конструктор

        wait = WebDriverWait(authorized_main_page, 5)
        header = wait.until(EC.visibility_of_element_located(ConstructorLocators.BURGER_HEADER))
        assert header.is_displayed()

    def test_click_logo(self, authorized_main_page):  # проверяем переход по логотипу Stellar Burgers
        authorized_main_page.find_element(*ConstructorLocators.PERSONAL_ACCOUNT_LINK).click()   # нажимаем кнопку личный кабинет
        authorized_main_page.find_element(*ConstructorLocators.LOGO_LINK).click()               # нажимаем логотип Stellar Burgers

        wait = WebDriverWait(authorized_main_page, 5)
        header = wait.until(EC.visibility_of_element_located(ConstructorLocators.BURGER_HEADER))
        assert header.is_displayed()