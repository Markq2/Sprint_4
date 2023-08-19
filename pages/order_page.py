from selenium.webdriver.common.by import By
from data.data import ORDER_PAGE_URL, MAIN_PAGE_URL
from helpers.helpers import *
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.locators import *
import allure


class OrderPage(BasePage):
    @allure.step('Клик по кнопке заказать в шапке сайта')
    def click_order_by_button(self, button):
        if button == 'header':
            BasePage.click(self, By.XPATH, HeaderLocators.header_order_button)
            BasePage.wait_for_url(self, ORDER_PAGE_URL)
        elif button == 'footer':
            BasePage.scroll_to_element(self, By.XPATH, MainPageLocators.footer_order_button)
            BasePage.click(self, By.XPATH, MainPageLocators.footer_order_button)
            BasePage.wait_for_url(self, ORDER_PAGE_URL)

    @allure.step('Заполнить поле Имя')
    def set_name_input(self):
        BasePage.fill_input(self, By.XPATH, OrderPageLocators.name_input, generate_random_name())

    @allure.step('Заполнить поле Фамилия')
    def set_lastname_input(self):
        BasePage.fill_input(self, By.XPATH, OrderPageLocators.lastname_input, generate_random_lastname())

    @allure.step('Заполнить поле Адрес')
    def set_address_input(self):
        BasePage.fill_input(self, By.XPATH, OrderPageLocators.address_input, generate_random_address())

    @allure.step('Заполнить поле Телефон')
    def set_phone_input(self):
        BasePage.wait_for_element(self, By.XPATH, OrderPageLocators.phone_input)
        BasePage.fill_input(self, By.XPATH, OrderPageLocators.phone_input, generate_random_phone())

    @allure.step('Выбор станции метро')
    def choose_metro_station(self):
        BasePage.click(self, By.XPATH, OrderPageLocators.metro_list)
        BasePage.click(self, By.XPATH, OrderPageLocators.metro_station)

    @allure.step('Клик по кнопке далее')
    def click_continue_button(self):
        BasePage.click(self, By.XPATH, OrderPageLocators.continue_button)

    @allure.step('Выбор даты')
    def set_date(self):
        BasePage.fill_input(self, By.XPATH, OrderPageLocators.date_input, BasePage.get_current_date(self))
        BasePage.press_button(self, By.XPATH, OrderPageLocators.date_input, Keys.ENTER)

    @allure.step('Выбор срока аренды')
    def choose_rent_period(self):
        BasePage.click(self, By.XPATH, OrderPageLocators.list_rent_period)
        BasePage.click(self, By.XPATH, OrderPageLocators.three_days_period)

    @allure.step('Выбор цвета самоката')
    def choose_color(self, color):
        if color == 'black':
            BasePage.click(self, By.ID, OrderPageLocators.black_color)
        elif color == 'gray':
            BasePage.click(self, By.ID, OrderPageLocators.gray_color)

    @allure.step('Клик по кнопке Заказать после ввода всех данных')
    def click_create_order(self):
        BasePage.click(self, By.XPATH, OrderPageLocators.create_order_button)

    @allure.step('Открытие формы заказа по кнопке, заполнение данных заказа')
    def create_order(self, button, color):
        self.click_order_by_button(button)
        self.set_lastname_input()
        self.set_address_input()
        self.set_name_input()
        self.set_phone_input()
        self.choose_metro_station()
        self.click_continue_button()
        self.set_date()
        self.choose_rent_period()
        self.choose_color(color)
        self.click_create_order()

    @allure.step('Клик по логотипу Самокат в шапке сайта')
    def click_on_yandex_logo(self):
        BasePage.click(self, By.CSS_SELECTOR, OrderPageLocators.samokat_logo)

    @allure.step('Проверка перехода на главную страницу Самоката при клике по логотипу в шапке сайта')
    def check_redirect_to_samokat_main_page(self):
        self.click_on_yandex_logo()
        BasePage.wait_for_url(self, 'MAIN_PAGE_URL')
        BasePage.wait_for_element(self, By.XPATH, HeaderLocators.header_order_button)
        if (BasePage.get_current_url(self) == MAIN_PAGE_URL and
                BasePage.check_for_element_visible(self, By.XPATH, HeaderLocators.header_order_button) is True):
            return True
        else:
            return 'Переход не произошел'

    @allure.step('Проверка успешного создания заказа')
    def check_order_created(self):
        BasePage.click(self, By.XPATH, OrderPageLocators.confirm_order_button)
        BasePage.wait_for_element(self, By.XPATH, OrderPageLocators.check_order_status_in_popup)
        if ('Заказ оформлен' in BasePage.get_text(self, By.XPATH,
                                                  OrderPageLocators.text_in_popup_header_after_confirm_order) and
                BasePage.check_for_element_visible(self, By.XPATH,
                                                   OrderPageLocators.check_order_status_in_popup) is True):
            return True
        else:
            return 'Заказ не оформлен'
