import pytest
from selene import browser, be, have
import pytest

@pytest.fixture
def open_brawser():
    browser.open('https://google.com')

def test_modification_google_search(open_brawser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_without_result(open_brawser):
    browser.element('[name="q"]').should(be.blank).type('adgasefASCAWERWERew').press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))
