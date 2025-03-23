from selene import browser, be, have


def test_search_in_duckduckgo(url, size_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[data-testid="result-title-a"]')
    browser.all('result').first.element('result-title-a')

    assert browser.should(have.title_containing('yashaka/selene'))
    print(' Значение "yashaka/selene" найдено на странице')


def test_not_search_in_duckduckgo(url, size_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[data-testid="result-title-a"]')
    browser.all('result').first.element('result-title-a')

    assert browser.should(have._not_.title_containing('java/java'))
    print(' Значение "java/java" не найдено на странице')