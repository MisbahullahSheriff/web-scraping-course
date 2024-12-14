import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

url = "https://www.google.com/"
driver.get(url)
time.sleep(1)

search_bar = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

search_bar.send_keys("machine learning")
time.sleep(1)

search_bar.send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()
