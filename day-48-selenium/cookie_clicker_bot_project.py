from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import threading
import time

chrome_driver_path = Service("X:\\Programming\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

secs_to_run = 5*60
timeout = time.time() + secs_to_run  # time from now
start_time = time.time()

def click_purchase():
    threading.Timer(5.0, click_purchase).start()
    store = driver.find_elements(By.CSS_SELECTOR, "#store [id^='buy']")  # ids starting with 'buy'
    for element in store[::-1]:
        if element.get_attribute('class') != "grayed":  # buy the most expensive element
            purchased_element_id = element.get_attribute("id")
            purchased_element = driver.find_element(By.ID, purchased_element_id)
            purchased_element.click()
click_purchase() 

cookie = driver.find_element(By.ID, "cookie")
while time.time() < timeout:
    cookie.click()
    time.sleep(0.05)

threading.Thread._stop
total_cookies = driver.find_element(By.ID, "money").text
print(f"cookies/second: {int(total_cookies)/secs_to_run:.2f}")