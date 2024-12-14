import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://github.com/login"
driver.get(url)
time.sleep(2)


class LoginPage:
	def __init__(self, driver):
		self.driver = driver
		self.username = (By.ID, "login_field")
		self.password = (By.ID, "password")
		self.login_button = (By.NAME, "commit")


	def login(self, username, password):
		self.driver.find_element(*self.username).send_keys(username)
		self.driver.find_element(*self.password).send_keys(password)
		time.sleep(1)
		self.driver.find_element(*self.login_button).click()


login_page = LoginPage(driver)
login_page.login("misbah", "pass123")

time.sleep(2)
driver.quit()