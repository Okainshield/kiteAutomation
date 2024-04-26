import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


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
td_element = driver.find_element(By.XPATH, "//td[contains(text(), '18018813725-Spin Master-Tech Deck-México-May')]")

# Wait for the status dropdown button to be visible and clickable, then click it
status_dropdown_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.filter_btn.active.dropdown-toggle.btn.btn-primary')))
status_dropdown_button.click()
time.sleep(3)

# Find the "Draft" status option and click it
draft_status_option = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'draft')))
draft_status_option.click()

# Check if the status has changed to "Draft" (you might need to adjust this condition based on your application)
# For example, if there is a confirmation that the status has changed, you can use that instead of a time.sleep()
time.sleep(3)  # Adjust this time as needed

# If the status has not changed to "Draft", select the "Pause" option
try:
    # Wait for the "Draft" status to be visible
    draft_status_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Draft')]")))
    # If "Draft" status is visible, click on the element to confirm the status change
    draft_status_element.click()
except TimeoutException:
    # If "Draft" status is not visible within the timeout period, select the "Pause" option
    # Wait for the status dropdown button to be visible and clickable, then click it
    status_dropdown_button = wait.until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, '.filter_btn.active.dropdown-toggle.btn.btn-primary')))
    status_dropdown_button.click()
    time.sleep(3)

    # Find the "Pause" status option and click it
    pause_status_option = wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, '.status_dropdown.media_plan_dropdown.status_design.dropdown .pause')))
    pause_status_option.click()
    time.sleep(3)

    # Wait for the confirmation pop-up to appear
    confirmation_popup = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'model_content')))
    # Click the "Confirm" button in the pop-up
    confirm_button = confirmation_popup.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]")
    confirm_button.click()
    time.sleep(6)  # Add a delay to allow the status change to be reflected in the UI


# close browser
driver.quit()
