import logging
import time
import utils

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium_utils import element

from urllib import parse

logger = logging.getLogger(__name__)


class Facebook:
    """
    Facebook automation tools on FireFoxProfile

    E.g: /Users/qhle/Library/Application Support/Firefox/Profiles/vzc6qzxv.default-release
         /Users/qhle/Library/Application Support/Firefox/Profiles/6h7m62vl.test1
    """

    def __init__(self, profile):
        self.profile = webdriver.FirefoxProfile(profile)
        self.driver = webdriver.Firefox(self.profile)

    def reviews_page(self, page, text, photo=''):
        """
        Reviews fanpage
        """
        logger.info('reviews_page: %s', page)
        try:
            # Input parameter
            reviews_url = page + '/reviews'

            # Redirect to Reviews
            self.driver.get(reviews_url)

            # Click button "Yes" from Recommend
            button_yes_locator = (By.XPATH, '//span[text()="Yes"]')
            utils.click(self.driver, button_yes_locator)

            # Enter text into editor
            editor_recommend_locator = (
                By.XPATH, '//div[contains(@aria-label, "What do you recommend about")]')
            utils.send_keys(self.driver, editor_recommend_locator, text)

            # Click button "Post"
            button_post_locator = (By.XPATH, '//span[text()="Post"]')
            utils.click(self.driver, button_post_locator)

            # Refresh page to get reviews
            self.driver.refresh()

            if photo:
                # Edit reviews
                actions_post_locator = (
                    By.XPATH, '//div[@aria-label="Actions for this post"]')
                utils.click(self.driver, actions_post_locator)

                button_edit_post_locator = (
                    By.XPATH, '//span[text()="Edit post"]')
                utils.click(self.driver, button_edit_post_locator)

                # Attachment photo/video
                add_photo_locator = (
                    By.XPATH, '//div[@aria-label="Photo/Video"]')
                utils.click(self.driver, add_photo_locator)

                input_add_photo_locator = (
                    By.XPATH, '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
                utils.send_keys(self.driver, input_add_photo_locator, photo)

                # Click "Save"
                button_save_locator = (By.XPATH, '//span[text()="Save"]')
                utils.click(self.driver, button_save_locator)

            logger.info('reviews_page done.')

        except exceptions.NoSuchElementException as e:
            logger.error('Element not found. %s', str(e))

    def comments_post(self, post, text, photo=''):
        """
        Comments post
        """
        logger.info('comments_post')

    def close(self):
        """
        Close browser
        """
        self.driver.close()


if __name__ == "__main__":
    profile = "/Users/qhle/Library/Application Support/Firefox/Profiles/vzc6qzxv.default-release"
    fb = Facebook(profile)
    content = "Shop nhiều đồ đáng yêu cực kỳ 🥰|/Users/qhle/Documents/Freelancer/python-test/data/review.jpg"
    split = content.split("|")
    text = split[0]
    photo = split[1]
    fb.reviews_page("https://www.facebook.com/pg/cavoi.danang", text, photo)
    time.sleep(5)
    # fb.close()
