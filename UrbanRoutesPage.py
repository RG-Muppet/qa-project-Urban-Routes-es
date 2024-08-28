from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import retrieve_phone_code
from selenium.webdriver.support import expected_conditions as EC


#Localizadores
class UrbanRoutesPage:
    #direcciones
    from_field = (By.ID, 'from')  #
    to_field = (By.ID, 'to')  #
    #seleccionar clase
    wait_for_taxi = (By.CLASS_NAME, 'modes-container')  #
    wait_for_class = (By.CLASS_NAME, 'tariff-picker shown')  #
    button_call_taxi = (By.CSS_SELECTOR, '.button.round')  #
    button_confort = (By.XPATH, '//*[@alt="Comfort"]')  #
    confirm_class_confort = (By.CSS_SELECTOR, '[data-for="tariff-card-4"]')
    #agregar telefóno
    phone_button = (By.CLASS_NAME, 'np-button')  #
    wait_format_phone = (By.CSS_SELECTOR, '.section.active')
    phone_input = (By.ID, 'phone')  #
    phone_save = (By.CSS_SELECTOR, '.button.full')
    wait_phone_code_format = (By.CSS_SELECTOR, '.section.active')
    phone_code = (By.ID, 'code')
    save_phone_code = (By.XPATH, '//*[text()="Confirmar"]')
    confirm_phone = (By.CLASS_NAME, 'np-text')
    #Agregar método de pago
    button_paymethod = (By.XPATH, '//*[@class="pp-text"]')
    wait_pay_method_select = (By.XPATH, '//div[@class="section active"]')
    button_add_card = (By.XPATH, '//*[text()="Agregar tarjeta"]')
    put_card_number = (By.CSS_SELECTOR, '#number')
    get_card_numbers = (By.XPATH, '//input[@placeholder="1234 4321 1408"]')
    Put_card_code = (By.XPATH, '//input[@placeholder="12"]')
    active_button = (By.CSS_SELECTOR, '.card-wrapper')
    save_card = (By.XPATH, '//*[text()="Agregar"]')
    close_pay_method_window = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    confirm_add_card = (By.CLASS_NAME, 'pp-value-text')
    #agregar comentario
    add_comment = (By.ID, 'comment')
    #Agregar manta y pañuelos
    add_manta = (By.CSS_SELECTOR, '.slider.round')
    manta_ok = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    #Agregar helados
    add_icecream = (By.XPATH, '(//div[@class="counter-plus"][1])')
    no_icecream = (By.XPATH, '(//div[@class="counter-value"][1])')
    # solicitar taxi e información de orden
    taxi_call = (By.CLASS_NAME, 'smart-button-secondary')
    wait_taxi = (By.XPATH, '//*[text()="Buscar automóvil"]')
    wait_order = (By.CLASS_NAME, 'order-number')


    def __init__(self, driver):
        self.driver = driver

    #1# Poner dirección de origen, detino.

    def wait_load_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.to_field))
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def wait_load_vehicles(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.wait_for_taxi))

#2# Seleccionar clase
    #clic en boton llamar taxi
    def push_call_taxi(self):
        return self.driver.find_element(*self.button_call_taxi).click()

    def wait_tariff_table(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.wait_for_class))

    def select_confort_class(self):
        return self.driver.find_element(*self.button_confort).click()

    def is_confort_class_selected(self):
        button_confort = self.driver.find_element(*self.confirm_class_confort)
        return "active" in button_confort.get_attribute("class")

    #3# Agregar número telefónico
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
    def confirm_add_phone(self):
        return self.driver.find_element(*self.confirm_phone).text

    #Agregar numero de tarjeta
    def add_card_number(self, card_number):
        return self.driver.find_element(*self.put_card_number).send_keys(card_number)

    #Agregar CVV de la tarjeta
    def add_cvv_card(self, card_code):
        return self.driver.find_element(*self.Put_card_code).send_keys(card_code)

    def get_card_number(self):
        return self.driver.find_element(*self.get_card_numbers).get_property('value')

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

    def confirm_card_pay_method(self):
        return self.driver.find_element(*self.confirm_add_card).text

    #agregar comentario
    def add_comment_driver(self, message_for_driver):
        return self.driver.find_element(*self.add_comment).send_keys(message_for_driver)

    def get_comment(self):
        return self.driver.find_element(*self.add_comment).get_property('value')

    def select_manta(self):
        self.driver.find_element(*self.add_manta).click()


    def confirm_manta(self):
        return self.driver.find_element(*self.manta_ok).get_property('checked')

    def add_one_icecream(self):
        return self.driver.find_element(*self.add_icecream).click()

    def get_number_icecream(self):
        icecream_text = self.driver.find_element(*self.no_icecream).text
        return int(icecream_text)

    def add_two_icecream(self):
        return self.driver.find_element(*self.add_icecream).click()
# Solicitar y ver información del taxi
    def call_taxi_now(self):
        return self.driver.find_element(*self.taxi_call).click()

    def search_taxi(self):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.wait_taxi))

    def order_information(self):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.wait_order))

    def information_taxi(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.wait_taxi)))

    def information_order(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.wait_order)))



