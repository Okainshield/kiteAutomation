import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Opening the Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 60)
driver.get('https://kite.kidscorp.digital/')
driver.maximize_window()

# Login Details
wait.until(ec.visibility_of_element_located((By.NAME, "email")))
username = driver.find_element(By.NAME, "email")
username.send_keys("fermin@kidscorp.digital")

password = driver.find_element(By.NAME, "password")
password.send_keys("faxter123")
btnLogin = driver.find_element(By.XPATH, "//button[@type='submit']")
btnLogin.click()

# Wait for the Campaign Manager element to be clickable and then click it
element = wait.until(ec.element_to_be_clickable((By.XPATH, "//li[@title='Campaign Manager']")))
element.click()
time.sleep(10)  # Added delay to ensure the page has loaded

# Click on the filter button for 'Market'
validation_data = [
    {"market_option": "Regional - Latam", "owner_option": "Sales", "sales_option": "Adriana", "status_option": "Active"},
    {"market_option": "ROLA", "owner_option": "Account", "status_option": "Inactive"},
    {"market_option": "México", "owner_option": "", "status_option": "Active"},
    {"market_option": "ROLA", "owner_option": "Adops", "status_option": "Active"}
]

for data in validation_data:

    market_filter_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Market')]")
    market_filter_button.click()
    time.sleep(2)  # Added delay to ensure the dropdown is visible

    market_option = driver.find_element(By.XPATH, f"//a[contains(text(), '{data['market_option']}')]")
    market_option.click()

    if data['owner_option']:
        owner_dropdown = WebDriverWait(driver, 15).until(
            ec.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropdown-toggle') and contains(text(), 'Owner')]"))
        )
        owner_dropdown.click()
        time.sleep(2)  # Added delay to ensure the dropdown is visible

        owner_option = WebDriverWait(driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{data['owner_option']}')]"))
        )
        owner_option.click()

    status_dropdown = WebDriverWait(driver, 30).until(
        ec.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropdown-toggle') and contains(text(), 'Status')]"))
    )
    status_dropdown.click()

    status_option = WebDriverWait(driver, 30).until(
        ec.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{data['status_option']}')]"))
    )
    status_option.click()

    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()

    # Wait for the search results to load
    time.sleep(30)  # Added delay to ensure the results are visible

    # To clear the previous data
    clear_button = WebDriverWait(driver, 30).until(
        ec.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'clear__btn1')]"))
    )
    clear_button.click()

# Close the browser
driver.quit()
