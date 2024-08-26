import data
from selenium import webdriver
from UrbanRoutesPage import UrbanRoutesPage


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
#1 Agregar dirección Origen-Destino
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.wait_load_page()
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.wait_load_vehicles()
        if routes_page.get_from() == address_from and routes_page.get_to() == address_to:
            print('Se agrego la dirección de origen East 2nd Street, 601 y la dirección destino 1300 1st St')

    # 2 Seleccionar clase confort
    def test_select_class(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.push_call_taxi()
        routes_page.select_confort_class()
        assert routes_page.is_confort_class_selected()
        if routes_page.is_confort_class_selected():
            print('Se selecciono la clase confort')

    # 3 Agregar número de telefono
    def test_add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        new_phone = data.phone_number
        routes_page.select_phone_space()
        routes_page.wait_format_phone_number()
        routes_page.put_phone(new_phone)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.next_phone()
        routes_page.wait_screen_phone_code()
        routes_page.put_code_phone()
        routes_page.click_confirm_code_button()
        assert routes_page.get_phone() == new_phone
        assert routes_page.confirm_add_phone() == new_phone
        if routes_page.get_phone() == new_phone:
            print('se ingreso el número +1 123 123 12 12')

    #4 Agregar método de pago
    def test_add_pay_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_pay_method()
        routes_page.click_pay_card()
        routes_page = UrbanRoutesPage(self.driver)
        new_card_number = data.card_number
        new_card_code = data.card_code
        routes_page.add_credit_card_numbers(new_card_number)
        routes_page.add_credit_card_codes(new_card_code)
        routes_page.active_save_card_button()
        routes_page.save_pay_card()
        routes_page.close_pay_method()
        assert routes_page.get_card_cvv() == new_card_code
        assert routes_page.get_card_number() == new_card_number
        assert routes_page.confirm_card_pay_method() == 'Tarjeta'
        if routes_page.get_card_number() == new_card_number and routes_page.get_card_cvv() == new_card_code and routes_page.confirm_card_pay_method() == 'Tarjeta':
            print('Se agrego la tarjeta con numero 1234 5678 9100 y CVV 111')

    # 5 Agregar comentario a conductor
    def test_add_comment_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        new_comment = data.message_for_driver
        routes_page.add_comment_driver(new_comment)
        assert routes_page.get_comment() == new_comment
        if routes_page.get_comment() == new_comment:
            print('Se ingreso el comentario correctamente')

    # 6 Seleccionar manta y pañuelos
    def test_add_manta_panuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_manta()
        print('Se solicitó manta y pañuelos correctamente.')

    # 7 Agregar dos helados
    def test_add_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_one_icecream()
        routes_page.add_two_icecream()
        assert routes_page.get_number_icecream() == 2
        if routes_page.get_number_icecream() == 2:
            print('Se agregaron dos helados')

    # 8 Solicitar taxi y ver información del taxi
    def test_call_taxi_see_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.call_taxi_now()
        routes_page.search_taxi()
        assert routes_page.information_taxi()
        routes_page.order_information()
        assert routes_page.information_order()
        print('Se mostro tiempo de espera del taxi e información del taxi')


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()