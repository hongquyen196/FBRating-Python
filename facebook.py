import logging
import time


from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium_utils import element

logger = logging.getLogger(__name__)

class Facebook:
    """
    Facebook mobile automation tools on FireFoxProfile

    E.g: /Users/qhle/Library/Application Support/Firefox/Profiles/vzc6qzxv.default-release
        /Users/qhle/Library/Application Support/Firefox/Profiles/6h7m62vl.test1
    """
    def __init__(self, profile):
        self.profile = webdriver.FirefoxProfile(profile)
        self.driver = webdriver.Firefox(self.profile)
    
    def reviews(self, page, content):
        try:
            # Input parameter
            reviews_url = page + "/reviews"
            split = content.split("|")
            text = split[0]
            photo = split[1]

            # Redirect to Reviews
            self.driver.get(reviews_url)

            # Click button "Yes" from Recommend
            button_yes_locator = (By.XPATH, '//button[@value="Yes" and @data-nt="FB:FDS_TETRA_BUTTON"]')
            button_yes = element.get_when_clickable(self.driver, button_yes_locator, 3)
            button_yes.click()

            # Enter text into textarea
            textarea_recommend_locator = (By.XPATH, '//textarea[@id="uniqid_1"]')
            textarea_recommend = element.get_when_visible(self.driver, textarea_recommend_locator, 3)
            textarea_recommend.send_keys(text)
            time.sleep(1)

            # Click button "Post"
            button_post_locator = (By.XPATH, '//button[@value="Post" and @type="submit"]')
            button_post = element.get_when_clickable(self.driver, button_post_locator, 3)
            button_post.click()
            time.sleep(1)

            # Get current URL https://mobile.facebook.com/home.php?s=100005682072873&sstr=1748514298681289&stype=s&postid=1748514298681289&gfid=AQAq_LjBn2jqvlt_Ujg&_rdr
            current_url = self.driver.current_url()
            print(current_url)

            # Attachment image
            if photo:
                reviewed_url = "https://mobile.facebook.com/story.php?story_fbid=1748514298681289&id=100005682072873"

                # Redirect to Reviewed URL
                self.driver.get(reviewed_url)

                # Click "..."

                # Click "Add photos"

                # Click "+ Photo"
                input_add_photo_locator = (By.XPATH, '//input[@accept="image/*"]')
                input_add_photo = element.get_when_visible(self.driver, input_add_photo_locator, 3)
                input_add_photo.send_keys(photo)

                # Click "Post"


        except exceptions.NoSuchElementException as e:
            logger.error("Element not found. %s", str(e))
        except :
            logger.error("Error when reviews.")




    def close(self):
        """
        """
        self.driver.close()


if __name__ == "__main__":
    profile = "/Users/qhle/Library/Application Support/Firefox/Profiles/vzc6qzxv.default-release"
    fb = Facebook(profile)
    fb.reviews("https://mobile.facebook.com/pg/cavoi.danang", "Shop nhiều đồ đáng yêu cực kỳ 🥰|/Users/qhle/Documents/Freelancer/python-test/data/review.jpg")
    time.sleep(5)
    # fb.close()

