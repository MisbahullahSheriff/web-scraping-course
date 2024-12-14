import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.miniclip.com/careers/vacancies'
driver.get(url)
time.sleep(2)

# identify the element
departments_field = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/section[2]/div/fieldset[3]/select')

# convert to dropdown element
departments_dropdown = Select(departments_field)

time.sleep(2)

# select option by index
departments_dropdown.select_by_index(5)

time.sleep(2)

# select option by display value
departments_dropdown.select_by_visible_text("Technology")

driver.quit()
