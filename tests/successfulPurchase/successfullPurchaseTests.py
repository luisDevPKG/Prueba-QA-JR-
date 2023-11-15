import unittest
import time
from utilities.utilities import WebDriverElements
from functions.successfulPurchase.successfulPurchase import SuccessfulPurchase


class SuccessfulPurchaseTests(unittest.TestCase):
    def setUp(self):
        self.driver_paths = WebDriverElements()
        self.driver = self.driver_paths.get_driver()
        self.driver.get("https://www.saucedemo.com/")

    # Caso de Prueba 1 : Compra exitosa de 1 solo producto
    def test_01_purchase_product(self):
        successfulPurchase = SuccessfulPurchase(self.driver)
        successfulPurchase.login('standard_user', 'secret_sauce')

        # Assert para validar que el usuario esté en la página principal
        expected_url = "https://www.saucedemo.com/inventory.html"
        real_url = successfulPurchase.dashboard_page()
        self.assertEqual(real_url, expected_url, f"El usuario NO puede iniciar sesion con credenciales Validas. "
                                                 f"Se esperaba que visualizara: '{expected_url}', pero se obtuvo: '{real_url}'.")

        successfulPurchase.choose_one_product()
        successfulPurchase.add_product()
        successfulPurchase.click_icon_shopping_cart()
        successfulPurchase.go_to_checkout_you_information()
        successfulPurchase.checkout_your_information_form('luis', 'mosquera', '410001')
        successfulPurchase.go_to_checkout_overview()
        successfulPurchase.go_to_checkout_complete()
        time.sleep(2)
        successfulPurchase.back_home()

    # Caso de Prueba 2: Ingesar 2 productos desde el dashboard,
    # eliminar uno, validar form Checkout your information y comprar 1 producto
    def test_02_purchase_product_dashboard(self):
        successfulPurchase = SuccessfulPurchase(self.driver)
        successfulPurchase.login('standard_user', 'secret_sauce')

        # Assert para validar que el usuario esté en la página principal
        expected_url = "https://www.saucedemo.com/inventory.html"
        real_url = successfulPurchase.dashboard_page()
        self.assertEqual(real_url, expected_url, f"El usuario NO puede iniciar sesion con credenciales Validas. "
                                                 f"Se esperaba que visualizara: '{expected_url}', pero se obtuvo: '{real_url}'.")

        successfulPurchase.choose_products_dashboard()
        successfulPurchase.click_icon_shopping_cart()
        time.sleep(1)
        # Assert para validar que se agregó el producto Sauce Labs Backpack
        expected_name = "Sauce Labs Backpack"
        name_text = successfulPurchase.product_one_cart_validator()
        self.assertEqual(name_text, expected_name, f"NO se agregó el producto correctamente. "
                                                   f"Se esperaba que el producto : '{expected_name}' se agregara al carrito")
        time.sleep(1)
        # Assert para validar que se agregó el producto Sauce Labs Bike Light
        expected_name2 = "Sauce Labs Bike Light"
        name2_text = successfulPurchase.product_two_cart_validator()
        self.assertEqual(name2_text, expected_name2, f"NO se agregó el producto correctamente. "
                                                     f"Se esperaba que el producto : '{expected_name2}' se agregara al carrito")
        successfulPurchase.remove_product()
        time.sleep(1)
        successfulPurchase.go_to_checkout_you_information()
        time.sleep(1)
        successfulPurchase.checkout_your_information_form('', '', '')
        successfulPurchase.go_to_checkout_overview()
        # Assert para validar la alerta campo First name requerido form checkout your information
        expected_alert_text = "Error: First Name is required"
        alert_text = successfulPurchase.first_name_required()
        self.assertEqual(alert_text, expected_alert_text, f"NO se está validando que el campo Firtst Name sea requerido. "
                                                          f"Se esperaba: '{expected_alert_text}', pero se obtuvo: '{alert_text}'.")
        time.sleep(1)
        successfulPurchase.checkout_your_information_form('luis', 'mosquera', '410001')
        successfulPurchase.go_to_checkout_overview()
        # Assert para validar que el producto a comprar sea Sauce Labs Bike Light
        expected_product = "Sauce Labs Bike Light"
        product_name = successfulPurchase.product_two_cart_validator()
        self.assertEqual(product_name, expected_product, f"Se eliminó el producto incorrecto. "
                                                         f"Se esperaba que el producto a comprar fuera : '{expected_product}'")
        successfulPurchase.go_to_checkout_complete()
        time.sleep(1)
        # Assert para validar mensaje de compra exitosa
        expected_message = "Thank you for your order!"
        message_text = successfulPurchase.message_purchase_successful()
        self.assertEqual(message_text, expected_message, f"Error, NO se completó la compra. "
                                                         f"El usuario debería visualizar: '{expected_message}', revisar manualmente")
        successfulPurchase.back_home()

    # Finaliza el test
    def tearDown(self):
        time.sleep(1)
        print('¡Se ha completado el Test Aumatico!')
        successfulPurchase = SuccessfulPurchase(self.driver)
        successfulPurchase.close()

    if __name__ == '__main__':
        unittest.main()