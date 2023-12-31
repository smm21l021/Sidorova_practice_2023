from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# зайти на страницу
# вбить юзернейм (standard_user)
# вбить пароль (secret_sauce)
# Нажать кнопку login
# добавить прогон тестов в CI


URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'


def open_page(driver, url):
    driver.get(url)


def input_data(driver, locator, data):
    input_field = driver.find_element(By.ID, locator)
    input_field.send_keys(data)


def click_button(driver, locator):
    button = driver.find_element(By.ID, locator)
    button.click()


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    return driver


driver_chrome = create_driver()
# 1
open_page(driver_chrome, URL)
# 2
input_data(driver_chrome, 'user-name', LOGIN)
# 3
input_data(driver_chrome, 'password', PASSWORD)
# 4
click_button(driver_chrome, 'login-button')
driver_chrome.quit()
# 5
