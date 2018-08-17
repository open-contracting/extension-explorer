import os

import pytest
from flask import url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.environ['FLASK_ENV'] = 'development'
BROWSER = os.environ.get('BROWSER', 'ChromeHeadless')


@pytest.fixture(scope="module")
def browser(request):
    if BROWSER == 'ChromeHeadless':
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(chrome_options=chrome_options)
    else:
        browser = getattr(webdriver, BROWSER)()
    browser.implicitly_wait(3)
    request.addfinalizer(lambda: browser.quit())
    return browser


@pytest.mark.usefixtures('live_server')
def test_to_test_selenium(browser):
    """
    Test to make sure selenium works.
    TODO Please delete when other tests are added.
    """
    browser.get(url_for('home', _external=True))

    text_body = browser.find_element_by_tag_name('body').text

    assert 'Extension Explorer' in text_body
