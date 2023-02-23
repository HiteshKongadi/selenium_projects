import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

d: WebDriver = webdriver.Chrome()

d.get("https://www.facebook.com")

# print the title of the page
print(d.title)

# email_element = d.find_element(By.ID,"email")
# email_element.send_keys("hello@xyz.com")

# Input values into the fields by identifying
d.find_element(By.ID, "email").send_keys("hello@xyz.com")
d.find_element(By.ID, "pass").send_keys("hello@123")

d.find_element(By.NAME, "login").click()

time.sleep(10)  # wait before closing the browse

d.quit()
