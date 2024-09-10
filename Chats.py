import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Chatsd:
    def __init__(self, driver):
        self.driver = driver

    def chatscrapper(self, link, button, listpath, listitem, span):
        self.driver.get(link)
        time.sleep(2)

        notify_close = self.driver.find_element(By.XPATH, button)
        notify_close.click()

        msg_list = self.driver.find_element(By.XPATH, listpath)
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", msg_list)
        chatters = []
        attempt = 0
        scroll_pause_time = 5

        while attempt < 5:
            chatting_elements = msg_list.find_elements(By.XPATH, listitem)
            # chatters.append(chatting_element.text for chatting_element in chatting_elements)
            for chatting_element in chatting_elements:
                chatter_info = {}
                try:
                    # Extracting username or relevant field
                    chatter_element = chatting_element.find_elements(By.XPATH, span)
                    username = chatter_element[0].text
                    chatter_info['username'] = username

                    # Extracting other info, such as message or time (example)
                    message = chatter_element[1].text
                    chatter_info['message'] = message

                except Exception as e:
                    print(f"Error extracting fields: {e}")

                # Add the dictionary to the list of chatters
                chatters.append(chatter_info)

            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', msg_list)
            time.sleep(scroll_pause_time)

            new_height = self.driver.execute_script("return arguments[0].scrollHeight", msg_list)
            if new_height == last_height:
                attempt += 1
            else:
                attempt = 0
            last_height = new_height
            # msg_user = driver.find_elements(By.XPATH, '//*[@id="mount_0_0_yt"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div')
            # msg_height = driver.execute_script("return arguments[0].scrollHeight", msg_user)

            # while True:
            # driver.execute_script('arguments[0]')

            # print(chatting_element.text)
        unique_chatters = set(tuple(chatter.items()) for chatter in chatters)
        unique_chatters = [dict(chatter) for chatter in unique_chatters]

        print(unique_chatters)
        print(len(unique_chatters))
        return unique_chatters
