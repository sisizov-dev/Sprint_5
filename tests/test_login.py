from selenium.webdriver.common.by import By
import time
def test_login_main_button(main_page, existing_user): #проверяем вход по кнопке «Войти в аккаунт» на главной странице
    main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click() # нажимаем кнопку войти в аккаунт

    #заполняем поля
    main_page.find_element(By.XPATH, "(//input[@name='name'])").send_keys(existing_user["email"])   #поле емайл
    main_page.find_element(By.NAME, "Пароль").send_keys(existing_user["password"])                     #поле пароль  

    main_page.find_element(By.XPATH, "//button[text()='Войти']").click() # нажимаем кнопку войти

    time.sleep(4) 
    assert len(main_page.find_elements(By.XPATH, "//button[contains(text(),'Оформить заказ')]")) > 0
    #assert main_page.find_element(By.XPATH, "//button[(text(),'Оформить заказ')]").is_displayed()
    #assert main_page.current_url == "https://stellarburgers.education-services.ru/"

def test_login_account_icon(main_page, existing_user): #проверяем вход через кнопку «Личный кабинет»
    main_page.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click() # нажимаем кнопку личный кабинет на главной странице

    #заполняем поля
    main_page.find_element(By.XPATH, "(//input[@name='name'])").send_keys(existing_user["email"])   #поле емайл
    main_page.find_element(By.NAME, "Пароль").send_keys(existing_user["password"])                     #поле пароль  

    main_page.find_element(By.XPATH, "//button[text()='Войти']").click() # нажимаем кнопку войти

    time.sleep(4) 
    assert len(main_page.find_elements(By.XPATH, "//button[contains(text(),'Оформить заказ')]")) > 0

def test_login_from_registration_page(main_page, existing_user): #проверяем в ход в личный кабинет через кнопку войти на стрнице регистрации
    main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click() # нажимаем кнопку войти в аккаунт
    main_page.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() # нажимаем кнопку зарегистрироваться
    main_page.find_element(By.XPATH, "//a[text()='Войти']").click()

    #заполняем поля
    main_page.find_element(By.XPATH, "(//input[@name='name'])").send_keys(existing_user["email"])   #поле емайл
    main_page.find_element(By.NAME, "Пароль").send_keys(existing_user["password"])                     #поле пароль  

    main_page.find_element(By.XPATH, "//button[text()='Войти']").click() # нажимаем кнопку войти

    time.sleep(4) 
    assert len(main_page.find_elements(By.XPATH, "//button[contains(text(),'Оформить заказ')]")) > 0