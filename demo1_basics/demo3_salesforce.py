

import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

d: WebDriver = webdriver.Chrome()

d.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")  # wait for the page load to complete
d.maximize_window()
d.implicitly_wait(30)  # synchronization time

d.find_element(By.NAME, "UserFirstName").send_keys("POlo")
d.find_element(By.NAME, "UserLastName").send_keys("dina")
select_title = Select(d.find_element(By.NAME,"UserTitle"))
select_title.select_by_visible_text("IT Manager")
select_emps = Select(d.find_element(By.NAME,"CompanyEmployees"))
select_emps.select_by_visible_text("101 - 500 employees")
#select_year = Select(d.find_element(By.ID,"year"))
#select_year.select_by_index("6")
d.find_element(By.NAME, "start my free trial").click()

time.sleep(10)

d.quit()
