import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://github.com/login'
driver.get(url)
time.sleep(2)

# username field
username_field = driver.find_element(By.ID, 'login_field')
username_field.send_keys('misbah')
time.sleep(1)

# password field
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('pass123')
time.sleep(1)

# submit button
submit_button = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
submit_button.click()
time.sleep(2)

driver.quit()
