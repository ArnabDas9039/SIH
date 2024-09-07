import time
from selenium.webdriver.common.by import By

def ChatScrap(driver):
    driver.get('https://www.instagram.com/direct/inbox/?hl=en')
    time.sleep(2)

    notify_close = driver.find_element(By.XPATH, '//div[@role="dialog"]//button[2]')
    notify_close.click()

    msg_list = driver.find_element(By.XPATH, '//div[@role="list"]/div/div/div')
    last_height = driver.execute_script("return arguments[0].scrollHeight", msg_list)
    chatters = set()
    attempt = 0
    scroll_pause_time = 5

    while attempt < 5:
        chatting_elements = msg_list.find_elements(By.XPATH, '//div[@role="listitem"]')
        # chatters.append(chatting_element.text for chatting_element in chatting_elements)
        for chatting_element in chatting_elements:
            name = chatting_element.text
            chatters.add(name)

        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', msg_list)
        time.sleep(scroll_pause_time)

        new_height = driver.execute_script("return arguments[0].scrollHeight", msg_list)
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

    print(chatters)
    print(len(chatters))