import pytest
from selene import browser, be, have


@pytest.fixture(scope="session")
def open_brawser():
    browser.open('https://google.com')
    yield
    browser.close()