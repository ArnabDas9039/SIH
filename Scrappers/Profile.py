import time
import requests
from selenium.webdriver.common.by import By

def ProfileScrap(driver, your_username):
    # Navigate to your profile
    driver.get('https://www.instagram.com/' + your_username + '/')
    time.sleep(2)

    profile_pic_element = driver.find_element(By.XPATH, '//img[contains(@alt, "profile")]')
    profile_pic_url = profile_pic_element.get_attribute('src')

    response = requests.get(profile_pic_url)
    if response.status_code == 200:
        with open('profile_picture.jpg', 'wb') as file:
            file.write(response.content)

    print(f"Profile picture downloaded successfully from {profile_pic_url}")