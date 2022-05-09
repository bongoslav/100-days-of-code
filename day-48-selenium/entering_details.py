from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("X:\\Programming\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
url = "https://secure-retreat-92358.herokuapp.com/"
driver.get(url)

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Borislav")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Borisov")
email = driver.find_element(By.NAME, "email")
email.send_keys("beborisov99@gmail.com")