import pytest
from selenium import webdriver
from data.data import MAIN_PAGE_URL


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(MAIN_PAGE_URL)
    yield browser
    browser.quit()
