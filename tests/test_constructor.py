from selenium.webdriver.common.by import By
import time
def test_sauces_section(main_page, authorized_main_page): # проверяем переход к разделу соусы
    main_page.find_element(By.XPATH, "//span[text()='Соусы']").click()

    time.sleep(2)
    assert main_page.find_element(By.XPATH, "//*[@alt='Соус фирменный Space Sauce']").is_displayed()