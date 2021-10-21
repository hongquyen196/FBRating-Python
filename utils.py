import time

from selenium_utils import element


def click(driver, locator, wait_seconds=3, sleep=1):
    """
    Args:
      driver  - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
      locator - Used to find the element
      wait_seconds - Timeout 3 seconds
      sleep - Sleep 1 second after click
    """
    element_clickable = element.get_when_clickable(
        driver, locator, wait_seconds)
    element_clickable.click()
    time.sleep(sleep)


def send_keys(driver, locator, value, wait_seconds=3, sleep=1):
    """
    Args:
      driver  - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
      locator - Used to find the element
      value - Data to send
      wait_seconds - Timeout 3 seconds
      sleep - Sleep 1 second after send keys
    """
    element_visible = element.get_when_visible(
        driver, locator, wait_seconds)
    element_visible.send_keys(value)
    time.sleep(sleep)
