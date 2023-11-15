from selenium.webdriver.common.by import By
from utilities import utilities


class LoginValidations:
    # defino los diferentes selectores
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.XPATH, "//input[@id='user-name']")
        self.password_locator = (By.XPATH, "//input[@id='password']")
        self.login_button_locator = (By.XPATH, "//input[@id='login-button']")
        self.locator_validator = (By.XPATH, "//div[@class='error-message-container error']")

    # Metodo para ingresar el username en el formulario
    def enter_user_name(self, username):
        self.driver.find_element(*self.username_locator).clear()
        self.driver.find_element(*self.username_locator).send_keys(username)

    # Metodo para ingresar el password en el formulario
    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).clear()
        self.driver.find_element(*self.password_locator).send_keys(password)

    # Método que hace clic en el boton del login
    def click_login_button(self):
        self.driver.find_element(*self.login_button_locator).click()

    # Método que valida que el userame sea obligatorio
    def user_name_required(self):
        return self.driver.find_element(*self.locator_validator).text

    # Método que valida que el Password sea obligatorio
    def user_password_required(self):
        return self.driver.find_element(*self.locator_validator).text

    # Método que realiza el proceso de login
    def login(self, username, password):
        self.enter_user_name(username)
        self.enter_password(password)
        self.click_login_button()

    # Finaliza el chrome driver
    def close(self):
        self.driver.close()