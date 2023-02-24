import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

select_day = Select(d.find_element(By.ID,"day"))
select_day.select_by_visible_text("20")
select_mnth = Select(d.find_element(By.ID,"month"))
select_mnth.select_by_value("12")
select_year = Select(d.find_element(By.ID,"year"))
select_year.select_by_index("6")


time.sleep(10)

d.quit()
