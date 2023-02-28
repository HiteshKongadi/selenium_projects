import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)


driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")

driver.find_element(By.XPATH, "//img[@alt='Go']").click()
#driver.find_element(By.LINK_TEXT, "Sign-In").click()
time.sleep(3)
actual_alert = driver.switch_to.alert.text
print(actual_alert)
driver.switch_to.alert.accept()

driver.find_element(By.XPATH, "//input[contains(@type,'text')]").send_keys("89205198")

time.sleep(5)
driver.quit()