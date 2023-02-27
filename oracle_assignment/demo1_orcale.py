import time

from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.oracle.com/in/database/")

driver.find_element(By.ID, "acctBtnLabel").click()
driver.find_element(By.LINK_TEXT, "Sign-In").click()

# print(driver.page_source)

time.sleep(5)

print(driver.title)

actual_header = driver.find_element(By.XPATH, "//h2[contains(text(),'Oracle account')]").text
print(actual_header)

driver.find_element(By.ID, "sso_username").send_keys("marco_polo@xyz.com")
driver.find_element(By.ID, "ssopassword").send_keys("hitesh")
driver.find_element(By.ID, "signin_button").click()
actual_error = driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text

for window in driver.window_handles:  # getting multiple window session ID
    print(window)
    driver.switch_to.window(window)
    print(driver.title)
    if "phpMyAdmin" in driver.title:
        break

    print('-' * 50)

time.sleep(5)
