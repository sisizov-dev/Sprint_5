from selenium.webdriver.common.by import By 
import time
def test_logout_from_personal_account(authorized_main_page): #проверяем проверяем кнопку выход из личного кабинета
    authorized_main_page.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click() #нажимаем кнопку личный кабинет
    authorized_main_page.find_element(By.XPATH, "//button[text()='Выход']").click()  # нажимаем кнопку выход из личного кабинета
    
    time.sleep(2)
    assert authorized_main_page.current_url == "https://stellarburgers.education-services.ru/login"