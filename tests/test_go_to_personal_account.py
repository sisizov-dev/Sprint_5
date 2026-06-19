import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginViaAccountLocators

class TestLoginViaAccount:
    def test_login_via_personal_account(self, main_page, existing_user):
        
        main_page.find_element(*LoginViaAccountLocators.PERSONAL_ACCOUNT_LINK).click() # нажимаем на кнопку "Личный Кабинет" на главной
        
        main_page.find_element(*LoginViaAccountLocators.EMAIL_INPUT_LOGIN).send_keys(existing_user["email"]) # вводим email
        
        main_page.find_element(*LoginViaAccountLocators.INP_PAS).send_keys(existing_user["password"]) # вводим пароль
        
        main_page.find_element(*LoginViaAccountLocators.SUBMIT_LOGIN).click() # нажимаем кнопку "Войти"
        
        # ожидаем появления кнопки "Оформить заказ" (явное ожидание)
        wait = WebDriverWait(main_page, 5)
        order_button = wait.until(EC.visibility_of_element_located(LoginViaAccountLocators.TITLE_ORDER))
        assert order_button.is_displayed()