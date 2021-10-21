# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import time


# _PROFILE = "/Users/qhle/Library/Application Support/Firefox/Profiles/6h7m62vl.test1"
# _PAGE = "https://www.facebook.com/Test1-107723814998302"


# profile = webdriver.FirefoxProfile(_PROFILE)
# driver = webdriver.Firefox(profile)

# # driver.get("http://www.python.org")
# # assert "Python" in driver.title
# # elem = driver.find_element_by_name("q")
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source˝


# def getFoxyProxy():
#     url = "https://addons.mozilla.org/vi/firefox/addon/foxyproxy-standard/"
#     driver.get(url)


# def getMBasic():
#     url = "https://mbasic.facebook.com/"
#     driver.get(url)
#     cookies = driver.get_cookies()
#     print(cookies)


# def getPage(page_url):
#     driver.get(page_url)


# def click(xpath):
#     element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, xpath)))
#     element.click()
#     time.sleep(1)


# def input(xpath, value):
#     element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, xpath)))
#     element.send_keys(value);


# def reviewPage(content):
#     click("//span[text()='Đánh giá']")
#     click("//span[text()='Đóng góp ý kiến']")
#     input("//label[@aria-label='Ý kiến đóng góp']//textarea", content)
#     click("//div[@role='dialog']//div[@role='button']//span[text()='Đóng góp ý kiến']")

# def createPost(content):
#     click("//span[text()='Tạo bài viết']")

    

# time.sleep(5)

# getPage(_PAGE)


# time.sleep(15)

# driver.close()
