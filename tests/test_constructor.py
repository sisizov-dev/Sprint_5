import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators

class TestConstructor:

    def test_sauces_section(self, authorized_main_page): # проверяем переход к разделу соусы
        authorized_main_page.find_element(*ConstructorLocators.SAUCES_TAB).click() #переходиим в раздел соусы

        wait = WebDriverWait(authorized_main_page, 5)
        active_tab = wait.until(EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert "Соусы" in active_tab.text

    def test_buns_section(self, authorized_main_page):  # проверяем переход к разделу булки
        authorized_main_page.find_element(*ConstructorLocators.SAUCES_TAB).click() #переходиим в раздел соусы
        authorized_main_page.find_element(*ConstructorLocators.BUNS_TAB).click() # переходим в раздел булки

        wait = WebDriverWait(authorized_main_page, 5)
        active_tab = wait.until(EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert "Булки" in active_tab.text

    def test_fillings_section(self, authorized_main_page):  # проверяем переход к разделу начинки
        authorized_main_page.find_element(*ConstructorLocators.FILLINGS_TAB).click() # переходим в раздел начинки

        wait = WebDriverWait(authorized_main_page, 5)
        active_tab = wait.until(EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert "Начинки" in active_tab.text