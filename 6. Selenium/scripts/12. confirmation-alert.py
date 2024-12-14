import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm"
driver.get(url)
time.sleep(2)

iframe_element = driver.find_element(By.ID, "iframeResult")
driver.switch_to.frame(iframe_element)

button = driver.find_element(By.XPATH, '/html/body/button')
button.click()

print(f"Alert Text: {driver.switch_to.alert.text}")

driver.switch_to.alert.accept()
print("\nYou clicked Accept!")
time.sleep(1)

# driver.switch_to.alert.dismiss()
# print("\nYou clicked Cancel!")
# time.sleep(1)

driver.switch_to.default_content()

driver.quit()