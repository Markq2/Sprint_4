import allure
import pytest
from data.data import ANSWERS
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка ответов на "Вопросы о важном" на главной странице')
    @pytest.mark.parametrize('question, answer', [(1, ANSWERS['1answer']),
                                                  (2, ANSWERS['2answer']),
                                                  (3, ANSWERS['3answer']),
                                                  (4, ANSWERS['4answer']),
                                                  (5, ANSWERS['5answer']),
                                                  (6, ANSWERS['6answer']),
                                                  (7, ANSWERS['7answer']),
                                                  (8, ANSWERS['8answer'])])
    def test_check_answers_on_main_page(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.scroll_page_down()
        main_page.question_click(question)
        assert answer == main_page.get_answer_text(question), "Ответ не соответствует ожидаемому"

    @allure.title('Проверка перехода на страницу Яндекс.Дзен при клике по логотипу Яндекс')
    def test_open_yandex_by_click_on_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo()
        assert main_page.check_redirect_to_dzen() is True
