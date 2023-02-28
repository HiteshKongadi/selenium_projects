import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://netbanking.hdfcbank.com/netbanking/")

# driver.find_element(By.NAME, "fldLoginUserId").click()


# actual_alert = driver.switch_to.alert.text
# print(actual_alert)
# driver.switch_to.alert.accept()

driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='login_page']"))
driver.find_element(By.XPATH, "//input[@name='fldLoginUserId']").send_keys("test123")
# driver.find_element(By.XPATH,"//a[contains(.,'CONTINUE')]").click()
driver.find_element(By.LINK_TEXT, "CONTINUE").click()


# switch to main html
driver.switch_to.default_content()

time.sleep(5)
