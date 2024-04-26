import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


def clear_form_data():
    driver.find_element(By.NAME, "name").clear()

    product_dropdown = driver.find_element(By.NAME, "product_id")
    product_dropdown.click()
    WebDriverWait(driver, 15).until(
        ec.element_to_be_clickable((By.XPATH, "//option[contains(text(), '--Select--')]"))
    ).click()
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "date_from").clear()
    driver.find_element(By.NAME, "date_to").clear()
    driver.find_element(By.NAME, "budge").clear()


# Opening the Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
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

# Find the search input field
search_input = driver.find_element(By.CSS_SELECTOR,
                                   ".cmn_header__search input[type='text'][placeholder='Search by Id or Advertiser']")

# Enter a value in the search input field
search_input.send_keys("18737736488")

# Press Enter key to perform the search
search_input.send_keys(Keys.ENTER)

# Wait for the search results to load
time.sleep(10)
# Perform actions on the search results
# For example, you can retrieve the search results using:
# search_results = driver.find_elements(By.XPATH, "//div[@class='your-search-results']/div")

# Find the table row element with cursor pointer style and click to open specific deal
element = driver.find_element(By.XPATH, "//tr[.//td[normalize-space() = 'Garfield - abril y mayo']]")
element.click()
time.sleep(10)

# click on Add New Campaign Button
element = driver.find_element(By.XPATH, "//button[contains(text(), 'Add New Campaign')]")
element.click()
time.sleep(5)

# Define test scenarios for form validation
validation_data = [
    {"name": "", "product": "", "date_from": "", "date_to": "", "budget": ""},
    {"name": "", "product": "HCL", "date_from": "25/04/2024", "date_to": "", "budget": "20000"},
    {"name": "Campaign 01", "product": "", "date_from": "", "date_to": "04/05/2024", "budget": "-30000"},
    {"name": "Campaign 06", "product": "Apple", "date_from": "25/04/2024", "date_to": "04/05/2024", "budget": "20000"}
    # Add more scenarios as needed
]

# Loop through each scenario
for data in validation_data:

    # Fill out the form fields
    driver.find_element(By.NAME, "name").send_keys(data["name"])

    product_dropdown = driver.find_element(By.NAME, "product_id")
    product_dropdown.click()
    product_option = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, f"//option[contains(text(), '{data['product']}')]"))
    )
    product_option.click()

    driver.find_element(By.NAME, "date_from").send_keys(data["date_from"])
    driver.find_element(By.NAME, "date_to").send_keys(data["date_to"])
    driver.find_element(By.NAME, "budge").send_keys(data["budget"])  # Corrected element name

    # Submit the form
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for a moment to see the result (you can add more validations here)
    time.sleep(4)

    # Check if data is saved
    try:
        WebDriverWait(driver, 15).until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except:
        # Data is saved, continue to next scenario
        pass

    # Clear the form before each scenario
    clear_form_data()
    time.sleep(10)

driver.quit()
