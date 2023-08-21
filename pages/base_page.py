from datetime import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.data import DZEN_URL, ORDER_PAGE_URL, MAIN_PAGE_URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, by, locator):
        element = self.driver.find_element(by, locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def wait_until_el_to_be_clickable(self, by, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((by, locator)))

    def check_for_element_visible(self, by, locator):
        return self.driver.find_element(by, locator).is_displayed()

    def click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def wait_for_element(self, by, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((by, locator)))

    def get_text(self, by, locator):
        return self.driver.find_element(by, locator).text

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_next_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def fill_input(self, by, locator, text):
        self.driver.find_element(by, locator).send_keys(text)

    def get_current_date(self):
        self.current_date = datetime.now().date()
        self.format_date = self.current_date.strftime("%d-%m-%Y")
        return self.format_date.replace('-', '.')

    def press_button(self, by, locator, button):
        self.driver.find_element(by, locator).send_keys(button)
