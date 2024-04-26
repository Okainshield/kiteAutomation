import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select  # import of Select
from selenium.webdriver.support import expected_conditions as ec

# Opening the Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
driver.get('https://kite.kidscorp.digital/')
driver.maximize_window()

# Login Details
wait.until(ec.visibility_of_element_located((By.NAME, "email")))
username = driver.find_element(By.NAME, "email")
username.send_keys("fermin@kidscorp.digital")
time.sleep(5)

password = driver.find_element(By.NAME, "password")
password.send_keys("faxter123")
time.sleep(5)
btnLogin = driver.find_element(By.XPATH, "//button[@type='submit']")
btnLogin.click()
time.sleep(5)

# Wait for the Campaign Manager element to be clickable and then click it
element = wait.until(ec.element_to_be_clickable((By.XPATH, "//li[@title='Campaign Manager']")))
element.click()
time.sleep(10)

# Click on the Deal ID row
rows = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//tr[contains(@style, 'cursor: pointer;')]")))
row_element = rows[3]  # Click on the fourth  element (index 4)
row_element.click()
time.sleep(5)

# click on the edit button of campaign with specified text

# Find the <td> element with the specified text
td_element = driver.find_element(By.XPATH, "//td[contains(text(), 'Update Campaign')]")

# Find the parent row of the <td> element
row_element = td_element.find_element(By.XPATH, "./parent::tr")

# Find the <div> element with the class "pdf_icon" within the row
div_element = row_element.find_element(By.XPATH, ".//div[@class='pdf_icon']")

# Click on the <div> element
div_element.click()
time.sleep(5)

# Find the Campaign Name input field and update its value
campaign_name_input = driver.find_element(By.NAME, "name")
campaign_name_input.clear()  # Clear existing value
campaign_name_input.send_keys("Update Campaign")  # Enter new value

# Find the Product dropdown and select the desired product
product_dropdown = driver.find_element(By.NAME, "product_id")
product_dropdown.click()
product_option = driver.find_element(By.XPATH, f"//option[@value='314643799']")
product_option.click()

# Find the Budget input field and update its value
budget_input = driver.find_element(By.NAME, "budge")
budget_input.clear()  # Clear existing value
budget_input.send_keys("90000")  # Enter new value

# Validate the budget range
budget = int(budget_input.get_attribute("value"))
if budget < 50000 or budget > 140000:
    print("Budget is not within the range of 50,000 and 140,000. Please correct it.")
    # You can choose to handle this error however you like, for example, raise an exception or return False
else:
    print("Budget is within the valid range.")

# Submit the form (assuming it's a button click or form submission)
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

# Wait for some time to see the updated data (you can adjust the time as needed)
time.sleep(5)

driver.quit()
