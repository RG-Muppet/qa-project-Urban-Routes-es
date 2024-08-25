import data
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from UrbanRoutesPage  import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()

    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        time.sleep(3)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.wait_load_vehicles()
        time.sleep(3)
        if routes_page.get_from() == address_from and routes_page.get_to() == address_to:
            print('La dirección de origen y destino se colocaron correctamente.')

    def test_call_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.push_call_taxi()
        print("Se hizo clic en el botón pedir taxi")

    def test_select_class_confort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_confort_class()
        time.sleep(3)
        print("Se selecciono la clase confort")

    def test_add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_phone_space()
        routes_page.wait_format_phone_number()
        time.sleep(3)
        print("Se abrio formato de nuevo número de telefono")

    def test_add_phone_number_code(self):
        routes_page = UrbanRoutesPage(self.driver)
        new_phone = data.phone_number
        routes_page.put_phone(new_phone)
        assert routes_page.get_phone() == new_phone
        if routes_page.get_phone() == new_phone:
            print('se ingreso el número de telefono correctamente')

    def test_add_next(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.next_phone()
        time.sleep(4)
        routes_page.wait_screen_phone_code()
        time.sleep(4)
        print("se paso a la ventana del código del teléfono")

    def test_code_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.put_code_phone()
        time.sleep(4)
        routes_page.click_confirm_code_button()
        time.sleep(4)
        print("Se agregó el código del teléfono correctamente")

    def test_add_pay_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_pay_method()
        time.sleep(4)
        routes_page.click_pay_card()
        time.sleep(4)
        print("Se selecciono el método de paga con tarjeta y se abrio el formulario")

    def test_add_credit_card_no(self):
        routes_page = UrbanRoutesPage(self.driver)
        new_card_number = data.card_number
        new_card_code = data.card_code
        routes_page.add_credit_card_numbers(new_card_number)
        routes_page.add_credit_card_codes(new_card_code)
        time.sleep(4)
        routes_page.active_save_card_button()
        routes_page.save_pay_card()
        time.sleep(4)
        routes_page.close_pay_method()
        assert routes_page.get_card_cvv() == new_card_code
        assert routes_page.get_card_number() == new_card_number
        if routes_page.get_card_number() == new_card_number and routes_page.get_card_cvv() == new_card_code:
            print('Se ingresó el número y CVV de la tarjeta correctamente')

    def test_add_comment_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        new_comment = data.message_for_driver
        routes_page.add_comment_driver(new_comment)
        time.sleep(4)
        assert routes_page.get_comment() == new_comment
        if routes_page.get_comment() == new_comment:
            print('Se ingreso el comentario correctamente')

    def test_scroll_to_tariff_picker(self):
        routes_page = UrbanRoutesPage(self.driver)
        scroll_bar = self.driver.find_element(By.CLASS_NAME, 'tariff-picker')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_bar)
        assert scroll_bar.is_displayed(), "El elemento 'tariff-picker' no es visible."

    def test_add_manta_panuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_manta()
        time.sleep(2)
        print('Se solicitó manta y pañuelos correctamente.')

    def test_add_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_one_icecream()
        routes_page.add_two_icecream()
        time.sleep(2)
        print('Se agregaron dos helados')

    def test_call_taxi_see_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.call_taxi_now()
        time.sleep(30)








    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
