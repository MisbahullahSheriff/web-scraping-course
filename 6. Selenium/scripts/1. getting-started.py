import time
from selenium import webdriver

# initialize the Chrome driver
driver = webdriver.Chrome()

# introduce delay of 10s
time.sleep(10)

# maximize the browser window
driver.maximize_window()

# accessing a webpage using URL
url = "https://www.google.com"
driver.get(url)

# printing meta-data of webpage
print(f"Title: {driver.title}")
print(f"Current URL: {driver.current_url}")

# capture screenshot of webpage
driver.save_screenshot("google-screenshot.png")
print("\nscreenshot taken!")

time.sleep(5)

# close the browser
driver.quit()