# Automatización de solicitud de taxi en Urban Routes

## Descripción del Proyecto

Este proyecto automatiza el proceso de solicitud de un taxi en la aplicación UrbanRoutes.
## Tecnologías y Técnicas Utilizadas

- **Lenguaje de programación**: Python
- **Automatización de pruebas**: Selenium WebDriver
- **Administración del navegador**: Chrome WebDriver
- **Manejo de Esperas**: `WebDriverWait` para gestionar esperas explícitas en elementos críticos del flujo de trabajo.
- **Obtención de localizadores**: Se obtubieron los localizadores a través de `Devtools`
  
## Instrucciones para Ejecutar las Pruebas

1. **Instalar packages**:
   - Instalar por medio python packages `selenium`, `pytest` y `webdriver-manager`

2. **Definir localizadores**:
   - Se definierón los localizadores de cada una de las partes interactuables en la aplicación web:
   - **set_from(from_address)**: Introduce la dirección de origen en el campo correspondiente.
- **set_to(to_address)**: Introduce la dirección de destino en el campo correspondiente.
- **get_from()**: Devuelve el valor actual del campo de dirección de origen.
- **get_to()**: Devuelve el valor actual del campo de dirección de destino.
- **set_route(address_from, address_to)**: Introduce las direcciones de origen y destino.
- **wait_load_vehicles()**: Espera hasta que se carguen las opciones de vehículos disponibles.
- **push_call_taxi()**: Hace clic en el botón para solicitar un taxi.
- **select_confort_class()**: Selecciona la opción de clase "Comfort".
- **select_phone_space()**: Selecciona el campo para introducir el número telefónico.
- **put_phone(phone_number)**: Introduce el número telefónico en el campo correspondiente.
- **get_phone()**: Devuelve el número de teléfono introducido.
- **next_phone()**: Hace clic en el botón para avanzar después de introducir el teléfono.
- **put_code_phone()**: Introduce el código de confirmación recibido.
- **click_confirm_code_button()**: Confirma el código de teléfono.
- **click_pay_method()**: Selecciona la opción de método de pago.
- **click_pay_card()**: Abre el formulario para introducir la tarjeta de crédito.
- **add_card_number(card_number)**: Introduce el número de tarjeta de crédito.
- **add_cvv_card(card_code)**: Introduce el código CVV de la tarjeta de crédito.
- **save_pay_card()**: Guarda la tarjeta de crédito introducida.
- **add_comment_driver(message_for_driver)**: Añade un comentario para el conductor.
- **select_manta()**: Solicita una manta.
- **add_one_icecream()**: Añade un helado a la solicitud.
- **call_taxi_now()**: Llama al taxi.

3. **Ejecutar las Pruebas**:
    - se ejecutaron las pruebas utilizando pytest y definiendo previament

4. **Descripción de las Pruebas**:
   - `test_set_route`: Verifica que las direcciones de origen y destino se establecen correctamente.
   - `test_call_taxi`: Simula el clic en el botón para llamar un taxi.
   - `test_select_class_confort`: Verifica la selección de la clase de taxi Comfort.
   - `test_add_phone_number`: Simula el ingreso de un número de teléfono.
   - `test_add_phone_number_code`: Verifica la introducción del código de verificación.
   - `test_add_pay_method`: Simula la selección de un método de pago y agrega una tarjeta de crédito.
   - `test_add_comment_to_driver`: Verifica la capacidad de agregar un comentario para el conductor.
   - `test_scroll_to_tariff_picker`: Verifica el desplazamiento hacia el selector de tarifas.
   - `test_add_manta_panuelos`: Simula la solicitud de una manta y pañuelos.
   - `test_add_icecream`: Verifica que se puedan agregar dos helados al pedido.
   - `test_call_taxi_see_information`: Verifica el flujo completo de solicitar un taxi y esperar la asignación.

