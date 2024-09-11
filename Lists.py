import time
from selenium.webdriver.common.by import By
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import main
import time


class Follow:
    def __init__(self,text,driver):
        self.followers_link = driver.find_element(By.PARTIAL_LINK_TEXT, text)
        self.driver = driver
        self.text = text

    def extract(self, Xpath):
        self.followers_link.click()
        time.sleep(2)

        # Scroll to load all followers
        # followers_panel = driver.find_element(By.XPATH, '//div[@role="dialog"]/div/div[2]/div/div/div[3]')
        followers_panel = self.driver.find_element(By.XPATH, Xpath)
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", followers_panel)

        while True:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_panel)
            time.sleep(2)
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", followers_panel)
            if new_height == last_height:
                break
            last_height = new_height

    def followers(self,panel,a,button):
        followers = []
        self.extract(panel)
        followers_elements = self.driver.find_elements(By.XPATH, a)
        for follower_element in followers_elements:
            name = follower_element.text
            followers.append(name)
        follower_close = self.driver.find_element(By.XPATH, button)
        follower_close.click()
        print("Number of "+self.text+": ", len(followers))
        print("List of "+self.text, followers)
        time.sleep(2)
        return followers


