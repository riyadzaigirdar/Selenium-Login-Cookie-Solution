import scrapy
from scrapy.selector import Selector
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from shutil import which
from time import sleep



PROXY = "144.217.101.245:3129"

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument('--remote-debugging-port=3129')

chrome_path = "/home/riyad/Desktop/kijji/kijji/spiders/chromedriver"

class KijSpider(scrapy.Spider):
    name = 'kij'
    
    
    def start_requests(self):
        self.j =1
        self.chrome = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        self.chrome.get(
            "https://www.kijiji.ca/b-grand-montreal/laptops/k0l80002?dc=true")
        sleep(50)
        self.chrome.get("https://www.kijiji.ca/t-login.html")
        self.chrome.find_element_by_name("emailOrNickname").send_keys(
            "riyad1401043@gmail.com")
        self.chrome.find_element_by_name("password").send_keys("riyad123456")
        self.chrome.find_element_by_xpath(
            "//*[@id='mainPageContent']/div/div/div/div/form/button").click()
        sleep(5)
        self.chrome.get(
            "https://www.kijiji.ca/b-grand-montreal/laptops/k0l80002?dc=true")
        sleep(5)

        html = self.chrome.page_source
        print("html string created")       
        selector = Selector(text=html)
        print("selector created")
        print(selector)
        links = selector.xpath("//a[@class='title ']/@href")
        print(links)
        for i in links:
            relative_link = i.extract()
            self.chrome.get("https://www.kijiji.ca"+relative_link)
            sleep(10)
            try:
                self.chrome.find_element_by_xpath("//*[@id='vip-body']/div[4]/button").click()
            except:
                pass
            
            try:
                self.chrome.find_element_by_xpath("//*[@id='vip-body']/div[6]/div[3]/div/div[3]/div/button").click()
            except:
                pass
            sleep(5)

            self.chrome.set_window_size(1500, 2500)
            # element = self.chrome.find_element_by_tag_name('body')
            # element.screenshot(f"test{j}.png")
            # element_png = element.screenshot_as_png
            self.chrome.save_screenshot(f"test{self.j}.png")
            # with open(f"test{self.j}.png", "wb") as file:
            #     file.write(element_png)
            self.j+=1
            
    def parse(self, response):
        pass

        # git@github.com:riyadzaigirdar/Selenium-Login-Cookie-Solution.git