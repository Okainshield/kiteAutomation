import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Opening the Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
driver.get('https://kite.kidscorp.digital/')
driver.maximize_window()

# Login Details
wait.until(EC.visibility_of_element_located((By.NAME, "email")))
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
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@title='Campaign Manager']")))
element.click()
time.sleep(10)

# Click on the Deal ID row
rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tr[contains(@style, 'cursor: pointer;')]")))
row_element = rows[3]  # Click on the fourth element (index 4)
row_element.click()
time.sleep(5)

# Find the <td> element with the specified text
td_element = driver.find_element(By.XPATH, "//td[contains(text(), '18018813725-Spin Master-Tech Deck-México-May')]")

# Define the list of scenarios
scenarios = [
    {"Status": "Active", "date": "2024/04/01"},
    {"date": "2024/03/01-2024/04/30"},
    {"Status": "Inactive", "date": "2024/03/18"}
]

# Iterate through the scenarios
for scenario in scenarios:
    # Clear the status field
    status_dropdown = driver.find_element(By.XPATH, "//button[contains(text(), 'Status')]")
    status_dropdown.click()

    # Clear the date field
    date_input = driver.find_element(By.CLASS_NAME, "form-control")
    date_input.click()

    if 'Status' in scenario:
        # Select the new status
        status_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{scenario['Status']}')]")))
        status_option.click()

    # Enter the new date
    date_input.send_keys(scenario.get("date"))

    # Click the apply button
    apply_button = driver.find_element(By.CLASS_NAME, "applyBtn")
    apply_button.click()

    # Click the search button
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()

    # Wait for the results to load
    time.sleep(5)

    # Clear the form for the next scenario
    clear_button = driver.find_element(By.XPATH, "//button[contains(@class, 'clear__btn1')]")
    clear_button.click()

# Close the browser
driver.quit()
