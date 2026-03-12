import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: en, es, fr, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nЗапуск браузера с языком: {language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()