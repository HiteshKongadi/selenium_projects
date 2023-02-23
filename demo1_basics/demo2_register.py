import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

d: WebDriver = webdriver.Chrome()

d.get("https://www.facebook.com")  # wait for the page load to complete
d.maximize_window()
d.implicitly_wait(30)  # synchronization time

d.find_element(By.LINK_TEXT, "Create new account").click()

d.find_element(By.NAME, "firstname").send_keys("Hello")
d.find_element(By.NAME, "lastname").send_keys("dina")
d.find_element(By.ID, "password_step_input").send_keys("password")
d.find_element(By.XPATH, "//input[@value='-1']").click()
d.find_element(By.NAME, "websubmit").click()
time.sleep(10)
