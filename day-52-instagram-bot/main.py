from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service("X:\\Programming\\chromedriver.exe")
SIMILAR_ACCOUNT = "gordongram"
USERNAME = ""
PASSWORD = ""

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_driver_path)
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.cookies_accept = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
        self.driver.cookies_accept.click()

        time.sleep(2)

        username_entry = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_entry.send_keys(USERNAME)

        password_entry = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_entry.send_keys(PASSWORD)
        password_entry.send_keys(Keys.ENTER)


    def find_followers(self):
        self.driver.get("https://www.instagram.com/gordongram/")
        followers_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        time.sleep(1)
        followers_button.click()
        time.sleep(1)
        followers_tab = self.driver.find_element(By.XPATH, "//div[@Class='isgrP']")
        # scroll
        for i in range(10):
            # executing some Javascript
            # scroll the top of the followers_tab (popup) element by the height of the followers_tab(popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_tab)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".PZuss li button")
        for element in follow_buttons:
            element.click()
            time.sleep(1)


bot = InstaFollower()

bot.login()
time.sleep(3)
bot.find_followers()
time.sleep(2)
bot.follow()