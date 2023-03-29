import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver: WebDriver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.openemr.io/b/openemr")
driver.find_element(By.ID, 'authUser').send_keys("admin")
driver.find_element(By.ID, 'clearPass').send_keys("pass")
select_lang = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
select_lang.select_by_visible_text("English (Indian)")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

driver.find_element(By.XPATH, "//div[contains(text(),'Patient')]").click()
driver.find_element(By.XPATH, "//div[contains(text(),'New/Search')]").click()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))
driver.find_element(By.ID, "form_fname").send_keys("patrick")
driver.find_element(By.ID, "form_lname").send_keys("Xavier")
driver.find_element(By.XPATH, "//input[@id='form_DOB']").send_keys("2023-03-01")
select_gender = Select(driver.find_element(By.XPATH, "//select[@id='form_sex']"))
select_gender.select_by_visible_text("Male")

driver.find_element(By.ID, "create").click()
# driver.find_element(By.XPATH,"//input[@value='Confirm Create New Patient']").click()
driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()
driver.switch_to.default_content()
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.alert_is_present())
# time.sleep(5)
# actual_alert = driver.switch_to.alert.text
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//iframe")

time.sleep(5)
driver.quit()
