from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
chrome_driver_path = Service("X:\\Programming\\chromedriver.exe")

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        # setting variables inside init so they are instance variable & can be accessed outside of the class
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        # consent to cookies
        self.consent_button = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        self.consent_button.click()
        self.go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        self.go_button.click()
        # extract down & up data
        speed_tester_progress = ".overall-progress"
        while True:
            time.sleep(1)
            progress = self.driver.find_element(By.CSS_SELECTOR, speed_tester_progress).text
            if progress.startswith("Your speed test has completed"):
                self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
                self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
                break
        # print data
        print(f"down: {self.down}\nup: {self.up}")

    def tweet_at_provider(self):
        url = "https://twitter.com/home"
        self.driver.get(url)
        # logging in
        time.sleep(3)
        self.email_entry = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        self.email_entry.send_keys(TWITTER_EMAIL)
        self.email_entry.send_keys(Keys.ENTER)
        time.sleep(3)
        self.password_entry = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password_entry.send_keys(TWITTER_PASSWORD)
        self.password_entry.send_keys(Keys.ENTER)
        # typing the message
        self.message_entry = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        self.message_entry.send_keys(f"A1, защо интернета ми е с down speed: {self.down} & up speed: {self.up}? Това е твърде бавно!")
        self.message_entry.send_keys(Keys.ENTER)


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
if float(bot.down) < 50 or float(bot.up) < 10:
    bot.tweet_at_provider()