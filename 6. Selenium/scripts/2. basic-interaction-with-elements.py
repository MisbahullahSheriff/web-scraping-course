import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

# access URL
url = 'https://www.google.com'
driver.get(url)
time.sleep(2)

# locating search bar
search_bar_xpath = '//*[@id="APjFqb"]'
search_bar = driver.find_element(by=By.XPATH, value=search_bar_xpath)

# enter input
search_bar.send_keys("machine learning")
time.sleep(1)

# clear fields
# search_bar.clear()
# time.sleep(1)

# simulating key press
search_bar.send_keys(Keys.ENTER)
time.sleep(2)

# clicking link
link_xpath = '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3'
link = driver.find_element(By.XPATH, link_xpath)
link.click()
time.sleep(2)

driver.quit()