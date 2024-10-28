import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="Yandex",
                     help="Выберите браузер: Yandex или Firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Выберите язык: ru, en or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "Yandex":
        binary_yandex_driver_file = r'C:\chromedriver\yandexdriver.exe'
        service = Service (executable_path=binary_yandex_driver_file)
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nЗапуск браузера Yandex для теста..")
        browser = webdriver.Chrome(service=service, options=options)
        browser.maximize_window()
        
    elif browser_name == "Firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nЗапуск браузера Firefox для теста..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name должно быть Chrome или Firefox")
    yield browser
    print("\nЗакрытие браузера..")
    browser.quit()