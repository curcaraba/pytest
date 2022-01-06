import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    if language_name == "es":
        print("\nstart browser with es language for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
        browser = webdriver.Chrome(options=options)
    elif language_name == "fr":
        print("\nstart browser with fr language for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()
