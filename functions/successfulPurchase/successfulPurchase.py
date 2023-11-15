from selenium.webdriver.common.by import By


class SuccessfulPurchase:
    # defino los diferentes selectores
    def __init__(self, driver):
        self.driver = driver

        #login
        self.username_locator = (By.XPATH, "//input[@id='user-name']")
        self.password_locator = (By.XPATH, "//input[@id='password']")
        self.login_button_locator = (By.XPATH, "//input[@id='login-button']")

        # products dashboard
        self.product_name_locator = (By.XPATH, "//div[@class='inventory_item_name '][contains(.,'Sauce Labs Backpack')]")

        # product info
        self.btn_add_cart_locator = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

        # shopping cart
        self.btn_shopping_cart = (By.XPATH, "//a[contains(@class,'shopping_cart_link')]")
        self.product_name_cart_locator = (By.XPATH, "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]")
        self.btn_remove_cart = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
        self.btn_continue_shopping_cart = (By.XPATH, "//button[@id='continue-shopping']")
        self.btn_checkout_cart = (By.XPATH, "//button[@id='checkout']")

        # Checkout your information
        self.first_name_locator = (By.XPATH, "//input[@id='first-name']")
        self.last_name_locator = (By.XPATH, "//input[@id='last-name']")
        self.zip_code_locator = (By.XPATH, "//input[@id='postal-code']")
        self.btn_cancel_locator = (By.XPATH, "//button[@id='cancel']")
        self.btn_continue_locator_checkout_yi = (By.XPATH, "//input[@id='continue']")

        # Checkout overview
        self.btn_finish_locator = (By.XPATH, "//button[@id='finish']")

        # Checkout Complete
        self.btn_back_home_locator = (By.XPATH, "//button[@id='back-to-products']")

    # Método para ingresar el username en el formulario
    def enter_user_name(self, username):
        self.driver.find_element(*self.username_locator).clear()
        self.driver.find_element(*self.username_locator).send_keys(username)

    # Método para ingresar el password en el formulario
    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).clear()
        self.driver.find_element(*self.password_locator).send_keys(password)

    # Método que hace clic en el boton del login
    def click_login_button(self):
        self.driver.find_element(*self.login_button_locator).click()

    # Método que valida que el usuario esté en la página principal
    def dashboard_page(self):
        return self.driver.current_url

    # Método que realiza el proceso de login
    def login(self, username, password):
        self.enter_user_name(username)
        self.enter_password(password)
        self.click_login_button()

    # Accede a la informacion del producto Sauce Labs Bike Light
    def choose_one_product(self):
        self.driver.find_element(*self.product_name_locator).click()

    # Agrega el producto
    def add_product(self):
        self.driver.find_element(*self.btn_add_cart_locator).click()

    # Hace clic en el icono del carrito de compras
    def click_icon_shopping_cart(self):
        self.driver.find_element(*self.btn_shopping_cart).click()

    # Hace clic en checkout para redirigir al usuario a Checkout Your information
    def go_to_checkout_you_information(self):
        self.driver.find_element(*self.btn_checkout_cart).click()

    # Ingresa firstname en el formulario de checkout your information
    def firtst_name_form(self, firstname):
        self.driver.find_element(*self.first_name_locator).clear()
        self.driver.find_element(*self.first_name_locator).send_keys(firstname)

    # Ingresa lastname en el formulario de checkout your information
    def last_name_form(self, lastname):
        self.driver.find_element(*self.last_name_locator).clear()
        self.driver.find_element(*self.last_name_locator).send_keys(lastname)

    # Ingresa Zip/Postal code en el formulario de checkout your information
    def zip_code_form(self, zipcode):
        self.driver.find_element(*self.zip_code_locator).clear()
        self.driver.find_element(*self.zip_code_locator).send_keys(zipcode)

    # LLena el formulario de checkout your information por completo
    def checkout_your_information_form(self, firstname, lastname, zipcode):
        self.firtst_name_form(firstname)
        self.last_name_form(lastname)
        self.zip_code_form(zipcode)

    # Hace clic en Continue para redirigir al usuario a Checkout Overview
    def go_to_checkout_overview(self):
        self.driver.find_element(*self.btn_continue_locator_checkout_yi).click()

    # Hace clic en Finish para redirigir al usuario a Checkout Complete
    def go_to_checkout_complete(self):
        self.driver.find_element(*self.btn_finish_locator).click()

    # Hace clic en Back Home para redirigir al usuario al dashboard de productos
    def back_home(self):
        self.driver.find_element(*self.btn_back_home_locator).click()

    # Finaliza el chrome driver
    def close(self):
        self.driver.close()
