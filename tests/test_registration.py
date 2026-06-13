from selenium.webdriver.common.by import By
def test_successful_registration(main_page, valid_user):

    main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click() # нажимаем кнопку войти в аккаунт

    main_page.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() # нажимаем кнопку зарегистрироваться

    #заполняем поля
    main_page.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(valid_user["name"])    #поле имя 
    main_page.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(valid_user["email"])   #поле емайл
    main_page.find_element(By.NAME, "Пароль").send_keys(valid_user["password"])                     #поле пароль  

    main_page.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click() # нажимаем кнопку зарегистрироваться

    assert main_page.find_element(By.XPATH, "//h2[contains(text(),'Вход')]").is_displayed()


# добавляем негативный тест с невалидным паролем
from selenium.webdriver.common.by import By
def test_registration_invalid_password(main_page, valid_user):

    valid_user["password"] = "123" 

    main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click() # нажимаем кнопку войти в аккаунт

    main_page.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() # нажимаем кнопку зарегистрироваться

    #заполняем поля
    main_page.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(valid_user["name"])    #поле имя 
    main_page.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(valid_user["email"])   #поле емайл
    main_page.find_element(By.NAME, "Пароль").send_keys(valid_user["password"])                     #поле пароль  

    main_page.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click() # нажимаем кнопку зарегистрироваться

    error_message = main_page.find_element(By.XPATH, "//p[contains(text(),'пароль')]")  # проверяем вывод сообщения об ошибке
    assert error_message.is_displayed()   