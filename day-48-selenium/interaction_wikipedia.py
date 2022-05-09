from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("X:\\Programming\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

# articles_num = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# articles_num.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Contributions")
# all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# driver.quit()