import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

# Setup WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
driver.get('https://kite.kidscorp.digital/home')
driver.maximize_window()

# Login Details
wait.until(ec.visibility_of_element_located((By.NAME, "email")))
username = driver.find_element(By.NAME, "email")
username.send_keys("fermin@kidscorp.digital")
time.sleep(5)

driver.quit()
