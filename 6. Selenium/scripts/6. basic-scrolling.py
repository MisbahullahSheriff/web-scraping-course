import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://en.wikipedia.org/wiki/Machine_learning"
driver.get(url)
time.sleep(2)

# scrolling to element
ai_xpath = '//*[@id="Artificial_intelligence"]'
ai_subtopic = driver.find_element(By.XPATH, ai_xpath)
driver.execute_script("arguments[0].scrollIntoView();", ai_subtopic)

# scrolling vertically
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(3)
driver.execute_script("window.scrollBy(0, -500);")

# scrolling by page height
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")