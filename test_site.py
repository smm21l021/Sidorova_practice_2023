from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# зайти на страницу
# вбить юзернейм (standard_user)
# вбить пароль (secret_sauce)
# Нажать кнопку login
# добавить прогон тестов в CI


URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

# 1
driver.get(URL)

# 2
login_input = driver.find_element(By.ID, 'user-name')
login_input.send_keys(LOGIN)
# 3
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys(PASSWORD)
# 4
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()
# 5
