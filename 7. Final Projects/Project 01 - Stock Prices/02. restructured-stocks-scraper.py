import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class StocksScraper:
	def __init__(self, driver, timeout=10):
		self.driver = driver
		self.wait = WebDriverWait(self.driver, timeout=timeout)
		self.data = []

    # wait while webpage loads
	def wait_for_page_to_load(self):
		page_title = self.driver.title
		try:
			self.wait.until(
				lambda d: d.execute_script("return document.readyState") == "complete"
			)
		except:
			print(f"The page \"{page_title}\" did not get fully loaded within the given duration.\n")
		else:
			print(f"The page \"{page_title}\" is fully loaded.\n")

	
    # access main url
	def access_url(self, url):
		self.driver.get(url)
		self.wait_for_page_to_load()


    # access most active stocks webpage
	def access_most_active_stocks(self):
		# hover to markets menu
		actions = ActionChains(self.driver)
		markets_menu = self.wait.until(
			EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]'))
		)
		actions.move_to_element(markets_menu).perform()
		
		# click on Trending Tickers
		trending_tickers = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]/div[1]/ul[1]/li[4]/a[1]/div[1]'))
		)
		trending_tickers.click()
		self.wait_for_page_to_load()
		
		# click on Most Active
		most_active = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[2]/main[1]/section[1]/section[1]/section[1]/article[1]/section[1]/div[1]/nav[1]/ul[1]/li[1]/a[1]/span[1]'))
		)
		most_active.click()
		self.wait_for_page_to_load()

    
    # extract data from all pages
	def extract_stocks_data(self):
		# extract data from webpage
		while True:
			self.wait.until(
				EC.presence_of_element_located((By.TAG_NAME, "table"))
			)
			rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
			for row in rows:
				values = row.find_elements(By.TAG_NAME, "td")
				stock = {
					"name": values[1].text,
					"symbol": values[0].text,
					"price": values[3].text,
					"change": values[4].text,
					"volume": values[6].text,
					"market_cap": values[8].text,
					"pe_ratio": values[9].text,
				}
				self.data.append(stock)
		
			# click next
			try:
				next_button = self.wait.until(
					EC.element_to_be_clickable((By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div/div[3]/div[3]/button[3]'))
				)
			except:
				print("The \"next\" button is not clickable. We have navigated through all the pages.")
				break
			else:
				next_button.click()
				time.sleep(1)


	def clean_and_save_data(self, filename="temp"):
		stocks_df = (
			pd
			.DataFrame(self.data)
			.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
			.assign(
				price=lambda df_: pd.to_numeric(df_.price),
				change=lambda df_: pd.to_numeric(df_.change.str.replace("+", "")),
				volume=lambda df_: pd.to_numeric(df_.volume.str.replace("M", "")),
				market_cap=lambda df_: df_.market_cap.apply(lambda val: float(val.replace("B", "")) if "B" in val else float(val.replace("T", "")) * 1000),
				pe_ratio=lambda df_: (
					df_
					.pe_ratio
					.replace("-", np.nan)
					.str.replace(",", "")
					.pipe(lambda col: pd.to_numeric(col))
				)
			)
			.rename(columns={
				"price": "price_usd",
				"volume": "volume_M",
				"market_cap": "market_cap_B"
			})
		)
		stocks_df.to_excel(f"{filename}.xlsx", index=False)


if __name__ == "__main__":
	driver = webdriver.Chrome()
	driver.maximize_window()

	url = "https://finance.yahoo.com/"
	scraper = StocksScraper(driver, 5)

	scraper.access_url(url)
	scraper.access_most_active_stocks()
	scraper.extract_stocks_data()
	scraper.clean_and_save_data("yahoo_finance-stocks")

	driver.quit()