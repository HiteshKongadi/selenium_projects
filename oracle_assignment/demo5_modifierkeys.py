import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver: WebDriver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://google.com")
#driver.find_element(By.)
actions = webdriver.ActionChains(driver)
actions.key_down(webdriver.Keys.SHIFT) \
    .send_keys("hello world").key_up(webdriver.Keys.SHIFT).pause(1) \
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1) \
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).send_keys(webdriver.Keys.ENTER)\
    .perform()


# driver.refresh()
time.sleep(5)
driver.quit()
