from selene import browser, be, have


def test_search_in_duckduckgo(url, size_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[data-testid="result-title-a"]')
    browser.all('result').first.element('result-title-a')

    assert browser.should(have.title_containing('yashaka/selene'))
    print(' По запросу "yashaka/selene" результаты найдены на странице')


def test_not_result_search_in_duckduckgo(url, size_browser):
    browser.element('[name="q"]').should(be.blank).type('hgfjkdghdfklghdkfjghfldgdf').press_enter()
    browser.element('[id="react-layout"]')

    assert browser.element('html').should(have.text('По запросу hgfjkdghdfklghdkfjghfldgdf результаты не найдены.'))
    print(' По запросу "hgfjkdghdfklghdkfjghfldgdf" результаты не найдены на странице')