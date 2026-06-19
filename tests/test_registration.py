import pytest
from selenium.webdriver.common.by import By
from locators import RegistrationLocators

class TestRegistration:
    def test_successful_registration(self, main_page, valid_user):

        main_page.find_element(*RegistrationLocators.BUTTON_ENTER).click() # нажимаем кнопку войти в аккаунт

        main_page.find_element(*RegistrationLocators.BUTTON_CHEK).click() # нажимаем кнопку зарегистрироваться

    #заполняем поля
        main_page.find_element(*RegistrationLocators.INP_NAME).send_keys(valid_user["name"])    #поле имя 
        main_page.find_element(*RegistrationLocators.INP_EMAIL).send_keys(valid_user["email"])   #поле емайл
        main_page.find_element(*RegistrationLocators.INP_PAS).send_keys(valid_user["password"]) #поле пароль  

        main_page.find_element(*RegistrationLocators.BUTTON_CHEKIN).click() # нажимаем кнопку зарегистрироваться

        assert main_page.find_element(*RegistrationLocators.TITLE_LOGIN).is_displayed() #ожидаем вывод на экран кнопки "Войти"


# добавляем негативный тест с невалидным паролем

    #def test_registration_invalid_password(main_page, valid_user):

     #   valid_user["password"] = "123" 

      #  main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click() # нажимаем кнопку войти в аккаунт

       # main_page.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() # нажимаем кнопку зарегистрироваться

    #заполняем поля
        #main_page.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(valid_user["name"])    #поле имя 
        #main_page.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(valid_user["email"])   #поле емайл
        #main_page.find_element(By.NAME, "Пароль").send_keys(valid_user["password"])                     #поле пароль  

        #main_page.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click() # нажимаем кнопку зарегистрироваться

        #error_message = main_page.find_element(By.XPATH, "//p[contains(text(),'пароль')]")  # проверяем вывод сообщения об ошибке
        #assert error_message.is_displayed()   