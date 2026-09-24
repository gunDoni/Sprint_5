from selenium.webdriver.common.by import By


# Главная страница
MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт»
ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")  # Кнопка «Личный кабинет»
CONSTRUCTOR_LINK = (By.CSS_SELECTOR, "a[href='/']")  # Ссылка «Конструктор» в шапке
LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 a")  # Логотип Stellar Burgers
BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка «Булки»
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка «Соусы»
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка «Начинки»
SAUCES_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]") # Активная вкладка «Соусы»
BUNS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]") # Активная вкладка «Булки»
FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]") # Активная вкладка «Начинки»

# Форма регистрации
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле «Имя»
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле «Email»
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")  # Поле «Пароль»
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
REGISTER_LOGIN_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")  # Ссылка «Войти» (переход на форму входа)
PASSWORD_ERROR_TEXT = (By.CSS_SELECTOR, ".input__error")  # Текст ошибки под полем пароля

# Форма входа
LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")  # Поле «Email»
LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")  # Поле «Пароль»
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка «Восстановить пароль»
LOGIN_REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться» (переход на форму регистрации)

# Форма восстановления пароля
FORGOT_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")  # Поле «Email»
RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка «Восстановить»
FORGOT_LOGIN_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")  # Ссылка «Войти»

# Личный кабинет

CONSTRUCTOR_LINK_BACK = (By.XPATH, ".//a[@href='/']//p[text()='Конструктор']")  # Ссылка «Конструктор» (переход обратно)
LOGOUT_BUTTON = (By.CLASS_NAME, "Account_button__14Yp3")  # Кнопка «Выйти»