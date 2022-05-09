from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service("X:\\Programming\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
url = "https://www.python.org/"
driver.get(url)


event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(0, len(event_times))}

print(events)




driver.quit()