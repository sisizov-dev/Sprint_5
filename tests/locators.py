from selenium.webdriver.common.by import By

class RegistrationLocators:
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка войти в аккаунт на главной странице
    BUTTON_CHEK = (By.CLASS_NAME, "Auth_link__1fOlj") #кнопка войти в аккаунт на главной странице

    INP_NAME = (By.XPATH, "(//input[@name='name'])[1]")    #поле имя 
    INP_EMAIL = (By.XPATH, "(//input[@name='name'])[2]")   #поле емайл
    INP_PAS =(By.NAME, "Пароль")                         #поле пароль 

    BUTTON_CHEKIN = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка зарегистрироваться в форме регистрации
    TITLE_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")
#main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click() # клик по кнопке войти в аккаунт на главной странице

#main_page.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() # клик по кнопке зарегистрироваться на странице входа в аккаунт

#заполннение полей
    #main_page.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(valid_user["name"])    #поле имя 
    #main_page.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(valid_user["email"])   #поле емайл
    #main_page.find_element(By.NAME, "Пароль").send_keys(valid_user["password"])                     #поле пароль  

#main_page.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click() # клик по кнопке зарегистрироваться на странице формы регистрации

#authorized_main_page.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click() #клик по кнопке личный кабинет на главной странице зарегистрированного пользователя

#authorized_main_page.find_element(By.XPATH, "//p[text()='Конструктор']").click() #клик по кнопке конструктор на главной странице зарегистрированного пользователя


#authorized_main_page.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click() #клик по логотипу Stellar Burgers

#authorized_main_page.find_element(By.XPATH, "//button[text()='Выход']").click()  # клик по кнопке выход из личного кабинета

#main_page.find_element(By.XPATH, "//button[text()='Войти']").click() # клик по кнопке войти в форме входа в личный кабинет

#authorized_main_page.find_element(By.XPATH, "//span[text()='Соусы']").click() # клик по кнопке переход в раздел соусы

#authorized_main_page.find_element(By.XPATH, "//span[text()='Булки']").click() # клик по кнопке переход в раздел булки

#authorized_main_page.find_element(By.XPATH, "//span[text()='Начинки']").click() # клик по кнопке переход в раздел начинки
#1