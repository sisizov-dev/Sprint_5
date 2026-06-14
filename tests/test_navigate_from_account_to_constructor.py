from selenium.webdriver.common.by import By 
import time
def test_click_constructor(authorized_main_page): #проверяем переход по кнопке конструктор
    authorized_main_page.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click() #нажимаем кнопку личный кабинет
    authorized_main_page.find_element(By.XPATH, "//p[text()='Конструктор']").click() #нажимаем кнопку конструктор

    time.sleep(2)
    assert (authorized_main_page.find_elements(By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))