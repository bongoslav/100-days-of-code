from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urljoin
import time
 

CHROME_DRIVER_PATH = "X:\\Programming\\chromedriver.exe"
WEB_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
          "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122" \
          ".17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible" \
          "%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22" \
          "%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22" \
          "%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse" \
          "%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max" \
          "%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C" \
          "%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D "
FORM_URL = "https://forms.gle/Ubc9YNGTSEjDL6Ke8"
 
options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
 
 
def get_lease_list():
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, "html.parser")
    return soup.select("ul li article")
 
 
def get_all_leases():
    driver.get(WEB_URL)
    time.sleep(4)
    lease_list = []
    # pagination and fetch data.(Up to page 4 for now)
    for page in range(1, 5):
        if page == 1:
            for _ in range(20):
                webdriver.ActionChains(driver).key_down(Keys.TAB).perform()
        for _ in range(120):
            webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
        lease_list.extend(get_lease_list())
        page_list = driver.find_elements_by_css_selector(".search-pagination a")[1:-1]
        page_list[page].click()
        time.sleep(2)
    # Convert to dictionary.
    lease_dic = {}
    for n in range(len(lease_list)):
        address = lease_list[n].select_one(".list-card-addr").getText()
        price = lease_list[n].select_one(".list-card-price").getText().split("/")[0].split("+")[0].replace("$", "").split(" ")[
            0]
        link = lease_list[n].select_one(".list-card-link").get("href")
        # get absolute path
        link = urljoin(WEB_URL, link)
        lease_dic.update({n: {"address": f"{address}", "price": f"{price}", "link": f"{link}"}})
    print(lease_dic)
    return lease_dic
 
# Fill out the form
def input_form(lease_dic):
    driver.get(FORM_URL)
    for lease in lease_dic.values():
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div["
                                     "1]/input").send_keys(f"{lease['address']}")
        driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div["
                                     "1]/input").send_keys(f"{lease['price']}")
        driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div["
                                     "1]/input").send_keys(f"{lease['link']}")
        driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span").click()
        time.sleep(2)
        driver.find_element_by_link_text("Send").click()
 
 
zillow_lease = get_all_leases()
input_form(zillow_lease)
 
driver.quit()
