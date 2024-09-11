import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import main
import time
import Lists
import Chats
options = webdriver.ChromeOptions()


options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.instagram.com')
time.sleep(2)
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
your_username = input("Enter username")
your_password = input("Enter Password")

username.send_keys(your_username)
password.send_keys(your_password)
password.send_keys(Keys.RETURN)

time.sleep(10)
driver.get('https://www.instagram.com/' + your_username + '/')
time.sleep(2)

profile_pic_element = driver.find_element(By.XPATH, '//img[contains(@alt, "profile")]')
profile_pic_url = profile_pic_element.get_attribute('src')

response = requests.get(profile_pic_url)
if response.status_code == 200:
    with open('profile_picture.jpg', 'wb') as file:
        file.write(response.content)

print(f"Profile picture downloaded successfully from {profile_pic_url}")


v1 = 'followers'
v2 = 'following'
followingpanel = '//div[@role="dialog"]/div/div[2]/div/div/div[4]'
followerpanel = '//div[@role="dialog"]/div/div[2]/div/div/div[3]'
#followerpanel = '//div[@role="dialog"]/div/div[4]'
#followingpanel = '//div[@role="dialog"]/div/div[4]'
followera = '//div[@role="dialog"]//a'
followerclose = '//div[@role="dialog"]//button'
follwersscrapper = Lists.Follow(v1,driver)
follwingscrapper = Lists.Follow(v2,driver)
followers = follwersscrapper.followers(followerpanel,followera,followerclose)
followings = follwingscrapper.followers(followingpanel,followera,followerclose)
followers.remove('')
print("Number of Followers: ",len(followers))
print("List of Followers", followers)

followings.remove('')
print("Number of Followings: ",len(followings))
print("List of Followings", followings)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find posts in the DOM
posts = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')

# Loop through each post
for post_index, post in enumerate(posts):
    post_url = post.get_attribute('href')
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(post_url)
    post_id = post_url.replace('https://www.instagram.com', '')

    time.sleep(2)

    try:
        media_elements = driver.find_element(By.XPATH, '//div[@role="button"]//img')
        media_element_time = driver.find_element(By.XPATH, f'//a[@href="{post_id}"]//time').get_attribute('datetime')

        print(media_element_time)
        # Handle multiple images or videos in a carousel post
        try:
            presentation = driver.find_element(By.XPATH, '//div[@role="presentation"]')
            media_index = 0
            unique_urls = set()
            while True:
                time.sleep(2)
                media_elements = presentation.find_elements(By.XPATH, "//li//img")

                for media_element in media_elements:
                    media_url = media_element.get_attribute('src')
                    unique_urls.add(media_url)
                try:
                    next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Next"]'))
                    )
                    next_button.click()
                    media_index += 1
                except Exception:
                    break

            # Download the images
            for media_index, media_url in enumerate(unique_urls):
                response = requests.get(media_url)
                if response.status_code == 200:
                    with open(f'post_{post_index + 1}_media_{media_index + 1}.jpg', 'wb') as file:
                        file.write(response.content)
                print(f"Post {post_index + 1}, media {media_index + 1} downloaded successfully from {media_url}")

        except Exception:
            media_url = media_elements.get_attribute('src')

            response = requests.get(media_url)
            if response.status_code == 200:
                with open(f'post_{post_index + 1}.jpg', 'wb') as file:
                    file.write(response.content)
            print(f"Post {post_index + 1} downloaded successfully from {media_url}")

    except Exception as e:
        print(f"Error processing post {post_index + 1}: {e}")

    # Close the current tab and switch back to the original tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


link = 'https://www.instagram.com/direct/inbox/?hl=en'
buttonpath = '//div[@role="dialog"]//button[2]'
listpath = '//div[@role="list"]/div/div/div'
listitem = '//div[@role="listitem"]'
span = './/span[@dir="auto"]'
chats = Chats.Chatsd(driver)
chatters = chats.chatscrapper(link,buttonpath,listpath,listitem,span)


driver.quit()
a = main.Processing(followings,followers,chatters)
a.process("chat.pdf","combined.pdf")