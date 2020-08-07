# import selenium
# from selenium import webdriver
# from time import sleep

# driver = webdriver.Chrome(
#     executable_path="./chromedriver", chrome_options="--proxy-server='144.217.101.245'")
# driver.get("https://www.duckduckgo.com")
# sleep(5)
# driver.close()


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PROXY = "144.217.101.245:3129"

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument('--remote-debugging-port=3129')

experimentalFlags = ['same-site-by-default-cookies@1',
                     'cookies-without-same-site-must-be-secure@1']
chromeLocalStatePrefs = {'browser.enabled_labs_experiments': experimentalFlags}
chrome_options.add_experimental_option('localState', chromeLocalStatePrefs)


class Kijibot:
    def __init__(self):
        # self.chrome = webdriver.Chrome(
        #     executable_path="./chromedriver", options=chrome_options)
        # print("requesting google")
        # self.chrome.get("https://www.duckduckgo.com")
        # input = self.chrome.find_element_by_xpath(
        #     "//*[@id='search_form_input_homepage']")
        # input.send_keys("kijji")
        # input.send_keys(Keys.ENTER)
        # link = self.chrome.find_element_by_xpath(
        #     "//*[@id='r1-0']/div/h2/a[1]")
        # link.click()
        # sleep(20)
        # self.chrome.find_element_by_xpath(
        #     "//*[@id='MainContainer']/div[1]/div/div[2]/div/header/div[3]/div/div[3]/div/div/div/a[2]").click()
        self.chrome = webdriver.Chrome(
            executable_path="./chromedriver", options=chrome_options)
        print("requesting start")
        self.chrome.get("https://www.kijiji.ca/t-login.html")

    def login(self):
        sleep(10)
        self.chrome.find_element_by_name("emailOrNickname").send_keys(
            "riyad1401043@gmail.com")
        self.chrome.find_element_by_name("password").send_keys("riyad123456")
        self.chrome.find_element_by_xpath(
            "//*[@id='mainPageContent']/div/div/div/div/form/button").click()
        sleep(5)

    def products_page(self):
        self.chrome.get(
            "https://www.kijiji.ca/b-grand-montreal/laptops/k0l80002?dc=true")
        self.list = self.chrome.find_elements_by_xpath(
            "https://www.kijiji.ca/b-grand-montreal/laptops/k0l80002?dc=true//*[@id='mainPageContent']/div/div/div/div/div/div/div/div[2]")

    def take_screenshot(self):
        print(self.list)


obj = Kijibot()
obj.login()
obj.products_page()
# emailOrNickname
# password
# //*[@id="mainPageContent"]/div/div/div/div/form/button
# https://www.kijiji.ca/b-grand-montreal/laptops/k0l80002?dc=true
# //*[@id="mainPageContent"]/div/div/div/div/div/div/div/div[2]
# element = driver.find_element_by_tag_name('body')
# element_png = element.screenshot_as_png
# with open("test2.png", "wb") as file:
#     file.write(element_png)

# Cookie “GCLB” will be soon rejected because it has the “sameSite” attribute set to “none” or an invalid value, without the “secure” attribute. To know more about the “sameSite“ attribute, read https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie/SameSite
