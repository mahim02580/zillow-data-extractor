import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

zillow_url = "ZILLOW_PAGE_URL"
form_url = "YOUR_FORM_URL"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7",
}
response = requests.get(zillow_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

house_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
house_link_list = [house_link_element["href"] for house_link_element in house_link_elements]
print(f"There are {len(house_link_list)} links to individual listings in total: \n")
print(house_link_list)

house_address_elements = soup.select("address[data-test='property-card-addr']")
house_address_list = [house_address_element.getText().strip().replace(" | ", " ") for house_address_element in
                      house_address_elements]
print(f"\n After having been cleaned up, the {len(house_address_list)} addresses now look like this: \n")
print(house_address_list)

house_price_elements = soup.select("span[data-test='property-card-price']")
house_price_list = [house_price_element.getText().replace("/mo", "").split("+")[0] for house_price_element in
                    house_price_elements]
print(f"\n After having been cleaned up, the {len(house_price_list)} prices now look like this: \n")
print(house_price_list)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(house_link_list)):
    driver.get(form_url)
    time.sleep(2)

    address_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(house_address_list[i])

    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(house_price_list[i])

    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(house_link_list[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
