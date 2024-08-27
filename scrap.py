import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
# options.add_argument('--auto-open-devtools-for-tabs')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.instagram.com')
time.sleep(2)

# Input your credentials
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

your_username = 'deekshaaa_ch'
your_password = 'gaynigga@69'

username.send_keys(your_username)
password.send_keys(your_password)
password.send_keys(Keys.RETURN)

time.sleep(10)  # Wait for login to complete

# Navigate to your profile
driver.get('https://www.instagram.com/' + your_username + '/')
#driver.get('https://www.instagram.com/dassauparna/')
time.sleep(2)

profile_pic_element = driver.find_element(By.XPATH, '//img[contains(@alt, "profile")]')
profile_pic_url = profile_pic_element.get_attribute('src')

response = requests.get(profile_pic_url)
if response.status_code == 200:
    with open('profile_picture.jpg', 'wb') as file:
        file.write(response.content)

print(f"Profile picture downloaded successfully from {profile_pic_url}")

# Click on the follower list
followers_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
followers_link.click()
time.sleep(2)

# Scroll to load all followers
followers_panel = driver.find_element(By.XPATH, '//div[@role="dialog"]/div/div[2]/div/div/div[3]')
last_height = driver.execute_script("return arguments[0].scrollHeight", followers_panel)

while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_panel)
    time.sleep(2)
    new_height = driver.execute_script("return arguments[0].scrollHeight", followers_panel)
    if new_height == last_height:
        break
    last_height = new_height

# Extract follower names
followers = []
followers_elements = driver.find_elements(By.XPATH, '//div[@role="dialog"]//a')
for follower_element in followers_elements:
    name = follower_element.text
    followers.append(name)

# Close the follower dialog
follower_close = driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
follower_close.click()
time.sleep(2)

# Click on the following list
following_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'following')
following_link.click()
time.sleep(2)

# Scroll to load all followers
following_panel = driver.find_element(By.XPATH, '//div[@role="dialog"]/div/div[2]/div/div/div[4]')
last_height = driver.execute_script("return arguments[0].scrollHeight", following_panel)

while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', following_panel)
    time.sleep(2)
    new_height = driver.execute_script("return arguments[0].scrollHeight", following_panel)
    if new_height == last_height:
        break
    last_height = new_height

# Extract follower names
followings = []
following_elements = driver.find_elements(By.XPATH, '//div[@role="dialog"]//a')
for following_element in following_elements:
    name = following_element.text
    followings.append(name)

# Close the following dialog
following_close = driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
following_close.click()
time.sleep(2)

followers.remove('')
print("Number of Followers: ",len(followers))
print("List of Followers", followers)

followings.remove('')
print("Number of Followings: ",len(followings))
print("List of Followings", followings)

while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',msg_list)
    time.sleep(2)
    new_height = driver.execute_script("return arguments[0].scrollHeight", msg_list)
    if new_height == last_height:
        break
    last_height = new_height
    # msg_user = driver.find_elements(By.XPATH, '//*[@id="mount_0_0_yt"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div')
    # msg_height = driver.execute_script("return arguments[0].scrollHeight", msg_user)

    # while True:
        # driver.execute_script('arguments[0]')


chatting_elements = msg_list.find_elements(By.XPATH, '//div[@role="listitem"]')
chatters = []
# chatters = [ chatting_element.text for chatting_element in chatting_elements]
print(chatting_elements)
for chatting_element in chatting_elements:
#     print(chatting_element)
    name = chatting_element.text
    chatters.append(name)

print(chatters)

# Close the browser
driver.quit()