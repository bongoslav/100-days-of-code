from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service("X:\\Programming\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# # amazon price tracker
# url = "https://www.amazon.com/Nilight-TL-42-Motorcycle-Waterproof-Multi-Color/dp/B08M31KKN2/ref=sr_1_5?crid=1CGU7J74DWI3G&keywords=motorcycle+led+strip&qid=1650784877&sprefix=motorcycle+led+strip%2Caps%2C193&sr=8-5"
# driver.get(url)
# price = driver.find_element(By.CSS_SELECTOR, "span.a-offscreen+span")  
# print(price.text)


# other
url = "https://www.python.org/"
driver.get(url)
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# CSS_SELECTOR: #id; .class tag
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[1]/a')
# print(link.text)



driver.quit()