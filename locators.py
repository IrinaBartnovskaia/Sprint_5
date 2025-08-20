from selenium.webdriver.common.by import By

class Locators:
    # форма регистрации
    NAME = (By.NAME, "name")  # поле ввода имя
    EMAIL = (By.XPATH, "//label[text()='Email']/following::input")  # поле ввода email
    PASSWORD = (By.NAME, "Пароль")  # поле ввода пароль
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class,'input__error') and contains(., 'Некорректный пароль')]")  # сообщение об ошибке
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка зарегистрироваться
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@href, '/login')]")  # кнопка войти

    # Форма авторизации
    SIGN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка войти
    REG_LINK = (By.XPATH, "//a[contains(@href, '/register')]")  # ссылка Зарегистрироваться
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[contains(@href, '/forgot-password')]")  # ссылка Восстановить пароль

    # Основная страница
    LOGO_LINK = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Личный кабинет
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка Выход

    # Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка Конструктор
    CONSTRUCTOR_TITLE = (By.XPATH, "h1[text()='Соберите бургер']") # Соберите бургер
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")  # секция Булки
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")  # секция Соусы
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")  # секция Начинки
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # активная вкладка
