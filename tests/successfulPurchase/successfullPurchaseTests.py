import unittest
import time
from utilities.utilities import WebDriverElements
from functions.successfulPurchase.successfulPurchase import SuccessfulPurchase


class SuccessfulPurchaseTests(unittest.TestCase):
    def setUp(self):
        self.driver_paths = WebDriverElements()
        self.driver = self.driver_paths.get_driver()
        self.driver.get("https://www.saucedemo.com/")

    # Caso de Prueba: Compra exitosa de 1 solo producto
    def test_02_purchase_product(self):
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
        successfulPurchase.back_home()

    # Finaliza el test
    def tearDown(self):
        time.sleep(1)
        print('¡Se ha completado el Test Aumatico!')
        successfulPurchase = SuccessfulPurchase(self.driver)
        successfulPurchase.close()

    if __name__ == '__main__':
        unittest.main()