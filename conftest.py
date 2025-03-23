import pytest

from selene import browser


@pytest.fixture(scope='function')
def url():
    browser.open('https://duckduckgo.com')

    yield

    print('Тест завершен')


@pytest.fixture()
def size_browser(url):
    browser.config.window_width = 1920
    browser.config.window_width = 1080
