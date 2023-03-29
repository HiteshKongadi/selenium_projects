import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver: WebDriver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.online.citibank.co.in/")

driver.find_element(By.XPATH, "//a[@title='Close']").click()
driver.find_element(By.LINK_TEXT, "Login").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, "//div[contains(@onclick,'ForgotUserID')]").click()
driver.find_element(By.CSS_SELECTOR, ".sbSelector").click()
driver.find_element(By.LINK_TEXT, "Credit Card").click()
driver.find_element(By.ID, 'citiCard1').send_keys('4567')
driver.find_element(By.ID, 'citiCard2').send_keys('4567')
driver.find_element(By.ID, 'citiCard3').send_keys('4567')
driver.find_element(By.ID, 'citiCard4').send_keys('4567')
#time.sleep(5)
driver.find_element(By.ID, 'cvvnumber').send_keys('457')
driver.find_element(By.ID, "bill-date-long").click()

# select_year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
# select_year.select_by_value('2023')


driver.execute_script("document.querySelector('#bill-date-long').value='11/02/2000'")

#driver.find_element(By.ID, 'agree').click()

driver.find_element(By.XPATH, "//input[@value='PROCEED']").click()
# select_month = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
time.sleep(5)
driver.quit()
