import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

d: WebDriver = webdriver.Chrome()

d.get("https://www.db4free.net/")  # wait for the page load to complete
d.maximize_window()
d.implicitly_wait(30)  # synchronization time

# d.find_element(By.XPATH, '//b[normalize-space()="phpMyAdmin »"]').click()
# d.find_element(By.LINK_TEXT, "phpMyAdmin").click()


d.find_element(By.PARTIAL_LINK_TEXT, "phpMyAdmin").click()

d.switch_to.window(d.window_handles[1])

d.find_element(By.ID, "input_username").send_keys("Hello")
d.find_element(By.ID, "input_password").send_keys("passw0rd`122")
d.find_element(By.ID, "input_go").click()
print(d.window_handles[1])
time.sleep(5)
d.close()

time.sleep(10)
d.quit()
