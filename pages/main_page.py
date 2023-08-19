from selenium.webdriver.common.by import By
from data.data import DZEN_URL
from pages.base_page import BasePage
from locators.locators import *
import allure


class MainPage(BasePage):
    @allure.step('Скролл страницы до вопросов')
    def scroll_page_down(self):
        BasePage.scroll_to_element(self, By.CSS_SELECTOR, MainPageLocators.questions)

    @allure.step('Клик по вопросу {question}')
    def question_click(self, question):
        BasePage.wait_until_el_to_be_clickable(self, By.ID, str(MainPageLocators.question + str(question - 1)))
        BasePage.click(self, By.ID, str(MainPageLocators.question + str(question - 1)))

    @allure.step('Получить текст ответа на вопрос {question}')
    def get_answer_text(self, question):
        BasePage.wait_for_element(self, By.ID, str(MainPageLocators.answer_text + str(question - 1)))
        return BasePage.get_text(self, By.ID, str(MainPageLocators.answer_text + str(question - 1)))

    @allure.step('Клик по логотипу Яндекс на главной')
    def click_on_yandex_logo(self):
        BasePage.click(self, By.CSS_SELECTOR, HeaderLocators.yandex_logo)

    @allure.step('Проверка перехода на страницу Яндекс Дзен')
    def check_redirect_to_dzen(self):
        BasePage.switch_to_next_window(self)
        BasePage.wait_for_url(self, 'dzen')
        BasePage.wait_for_element(self, By.XPATH, YandexDzenLocators.page_header)
        if (BasePage.check_for_element_visible(self, By.XPATH, YandexDzenLocators.page_header) is True and
                BasePage.get_current_url(self) == DZEN_URL):
            return True
        else:
            return 'Переход не произошел'
