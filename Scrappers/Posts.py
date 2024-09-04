import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def PostScrap(driver, your_username):
    # Navigate to your profile
    driver.get("https://www.instagram.com/" + your_username + "/")
    time.sleep(2)

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
        post_url = post.get_attribute("href")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(post_url)
        post_id = post_url.replace("https://www.instagram.com", "")

        time.sleep(2)

        try:
            media_elements = driver.find_element(By.XPATH, '//div[@role="button"]//img')
            media_element_time = driver.find_element(
                By.XPATH, f'//a[@href="{post_id}"]//time'
            ).get_attribute("datetime")

            print(media_element_time)
            # Handle multiple images or videos in a carousel post
            try:
                presentation = driver.find_element(
                    By.XPATH, '//div[@role="presentation"]'
                )
                media_index = 0
                unique_urls = set()
                while True:
                    time.sleep(2)
                    media_elements = presentation.find_elements(By.XPATH, "//li//img")

                    for media_element in media_elements:
                        media_url = media_element.get_attribute("src")
                        unique_urls.add(media_url)
                    try:
                        next_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, '//button[@aria-label="Next"]')
                            )
                        )
                        next_button.click()
                        media_index += 1
                    except Exception:
                        break

                # Download the images
                for media_index, media_url in enumerate(unique_urls):
                    response = requests.get(media_url)
                    if response.status_code == 200:
                        with open(
                            f"post_{post_index + 1}_media_{media_index + 1}.jpg", "wb"
                        ) as file:
                            file.write(response.content)
                    print(
                        f"Post {post_index + 1}, media {media_index + 1} downloaded successfully from {media_url}"
                    )

            except Exception:
                media_url = media_elements.get_attribute("src")

                response = requests.get(media_url)
                if response.status_code == 200:
                    with open(f"post_{post_index + 1}.jpg", "wb") as file:
                        file.write(response.content)
                print(f"Post {post_index + 1} downloaded successfully from {media_url}")

        except Exception as e:
            print(f"Error processing post {post_index + 1}: {e}")

        # Close the current tab and switch back to the original tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
