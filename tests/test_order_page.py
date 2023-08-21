import pytest
import allure
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка перехода на главную страницу Самоката при клике по логотипу Самоката')
    def test_open_samokat_main_page_by_click_on_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_by_button('header')
        assert order_page.check_redirect_to_samokat_main_page() is True

    @allure.title('Проверка заказа через кнопки в шапке и в подвале сайта, выбирая разные цвета самоката')
    @pytest.mark.parametrize('button, color', [('header', 'black'), ('footer', 'gray')])
    def test_success_order_by_buttons_with_different_colors(self, driver, button, color):
        order_page = OrderPage(driver)
        order_page.create_order(color=color, button=button)
        assert order_page.check_order_created() is True
