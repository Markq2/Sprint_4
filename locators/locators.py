class MainPageLocators:
    footer_order_button = "//div[contains(@class, 'Finish')]//button[text()='Заказать']"
    questions = '[class="accordion"]'
    question = 'accordion__heading-'
    answer_text = 'accordion__panel-'


class HeaderLocators:
    header_order_button = "//div[contains(@class, 'Header')]//button[text()='Заказать']"
    yandex_logo = '[alt="Yandex"]'


class OrderPageLocators:
    name_input = "//*[contains(@placeholder, 'Имя')]"
    lastname_input = "//*[contains(@placeholder, 'Фамилия')]"
    address_input = "//*[contains(@placeholder, 'Адрес')]"
    phone_input = "//*[contains(@placeholder, 'Телефон')]"
    metro_list = "//*[contains(@placeholder, 'Станция метро')]"
    metro_station = '//*[contains(text(), "Черкизовская")]'
    samokat_logo = 'img[alt="Scooter"]'
    continue_button = "//*[contains(text(), 'Далее')]"
    date_input = "//*[contains(@placeholder, 'Когда')]"
    list_rent_period = "//div[contains(@class, 'Dropdown-root')]"
    three_days_period = "//*[contains(text(), 'трое суток')]"
    gray_color = 'grey'
    black_color = 'black'
    create_order_button = "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"
    close_datepicker = '[src="/assets/calendar.svg"]'
    confirm_order_button = "//button[contains(text(), 'Да')]"
    check_order_status_in_popup = "//button[contains(text(), 'Посмотреть статус')]"
    text_in_popup_header_after_confirm_order = "//div[contains(@class, 'ModalHeader')]"


class YandexDzenLocators:
    page_header = "//div[contains(text(),'Новости')]"
