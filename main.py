import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

time.sleep(5)


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


#Localizadores
class UrbanRoutesPage:
    from_field = (By.ID, 'from')  #
    to_field = (By.ID, 'to')  #
    wait_for_taxi = (By.CLASS_NAME, 'modes-container')  #
    wait_for_class = (By.CLASS_NAME, 'tariff-picker shown')  #
    button_call_taxi = (By.CSS_SELECTOR, '.button.round')  #
    button_confort = (By.XPATH, '//*[@alt="Comfort"]')  #
    phone_button = (By.CLASS_NAME, 'np-button')  #
    wait_format_phone = (By.CSS_SELECTOR, '.section.active')
    phone_input = (By.ID, 'phone')  #
    phone_save = (By.CSS_SELECTOR, '.button.full')
    wait_phone_code_format = (By.CSS_SELECTOR, '.section.active')
    phone_code = (By.ID, 'code')
    save_phone_code = (By.XPATH, '//*[text()="Confirmar"]')
    button_paymethod = (By.XPATH, '//*[@class="pp-text"]')
    wait_pay_method_select = (By.XPATH, '//div[@class="section active"]')
    button_add_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    put_card_number = (By.CSS_SELECTOR, '#number')
    Put_card_code = (By.XPATH, '//input[@placeholder="12"]')
    active_button = (By.CSS_SELECTOR, '.card-wrapper')
    save_card = (By.XPATH, '//*[text()="Agregar"]')
    close_pay_method_window = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    add_comment = (By.ID, 'comment')
    add_manta = (By.CSS_SELECTOR, '.slider.round')
    scroll_bar = (By. CLASS_NAME, 'tariff-picker shown')
    add_icecream = (By.XPATH, '(//div[@class="counter-plus"][1])')
    taxi_call = (By.CLASS_NAME, 'smart-button-secondary')


    def __init__(self, driver):
        self.driver = driver

    #1
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    #2
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    #3
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    #4
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #5
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    #6
    def wait_load_vehicles(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.wait_for_taxi))

    #7
    #clic en boton llamar taxi
    def push_call_taxi(self):
        return self.driver.find_element(*self.button_call_taxi).click()

    #8
    def wait_tariff_table(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.wait_for_class))

    #9
    #clic en confort
    def select_confort_class(self):
        return self.driver.find_element(*self.button_confort).click()

    #Clic en la casilla telefono
    def select_phone_space(self):
        return self.driver.find_element(*self.phone_button).click()

    def wait_format_phone_number(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.wait_format_phone))

    #Intoducir telefono
    def put_phone(self, phone_number):
        return self.driver.find_element(*self.phone_input).send_keys(phone_number)

    def get_phone(self):
        return self.driver.find_element(*self.phone_input).get_property('value')

    #Clic siguiente en casilla telefono
    def next_phone(self):
        return self.driver.find_element(*self.phone_save).click()

    def wait_screen_phone_code(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.wait_phone_code_format))

    #Poner código de verificación
    def put_code_phone(self):
        code = retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.phone_code))
        return self.driver.find_element(*self.phone_code).send_keys(code)

    #Confirmar el código del telefono
    def click_confirm_code_button(self):
        return self.driver.find_element(*self.save_phone_code).click()

    #Seleccionar casilla "metodo de pago"
    def click_pay_method(self):
        return self.driver.find_element(*self.button_paymethod).click()

    def wait_pay(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.wait_pay_method_select))

    #Clic agregar tarjeta
    def click_pay_card(self):
        return self.driver.find_element(*self.button_add_card).click()

    #Agregar numero de tarjeta
    def add_card_number(self, card_number):
        return self.driver.find_element(*self.put_card_number).send_keys(card_number)

    #Agregar CVV de la tarjeta
    def add_cvv_card(self, card_code):
        return self.driver.find_element(*self.Put_card_code).send_keys(card_code)

    def get_card_number(self):
        return self.driver.find_element(*self.put_card_number).get_property('value')

    def get_card_cvv(self):
        return self.driver.find_element(*self.Put_card_code).get_property('value')

    def add_credit_card_numbers(self, card_number):
        self.add_card_number(card_number)

    def add_credit_card_codes(self, card_code):
        self.add_cvv_card(card_code)

    def active_save_card_button(self):
        return self.driver.find_element(*self.active_button).click()

    #Guardar tarjeta
    def save_pay_card(self):
        return self.driver.find_element(*self.save_card).click()

    def close_pay_method(self):
       return self.driver.find_element(*self.close_pay_method_window).click()

    #agregar comentario
    def add_comment_driver(self, message_for_driver):
        return self.driver.find_element(*self.add_comment).send_keys(message_for_driver)

    def get_comment(self):
            return self.driver.find_element(*self.add_comment).get_property('value')

    def scroll_bar_full(self, scroll_bar):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_bar)

    def select_manta(self):
        return self.driver.find_element(*self.add_manta).click()

    def add_one_icecream(self):
        return self.driver.find_element(*self.add_icecream).click()
    def add_two_icecream(self):
        return self.driver.find_element(*self.add_icecream).click()

    def call_taxi_now(self):
        return self.driver.find_element(*self.taxi_call).click()


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
