from selenium.webdriver.common.by import By
import time
def test_sauces_section(authorized_main_page): # проверяем переход к разделу соусы
    authorized_main_page.find_element(By.XPATH, "//span[text()='Соусы']").click() # переходим в раздел соусы

    time.sleep(2)
    assert authorized_main_page.find_element(By.XPATH, "//*[@alt='Соус фирменный Space Sauce']").is_displayed()

def test_buns_section(main_page, authorized_main_page):  # проверяем переход к разделу булки
    authorized_main_page.find_element(By.XPATH, "//span[text()='Соусы']").click() # переходим в раздел соусы
    authorized_main_page.find_element(By.XPATH, "//span[text()='Булки']").click() # переходим в раздел булки

    time.sleep(2)
    assert authorized_main_page.find_element(By.XPATH, "//*[@alt='Флюоресцентная булка R2-D3']").is_displayed()