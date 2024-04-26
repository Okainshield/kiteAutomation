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

# List of test cases
test_cases = [
    {"email": "wrong@example.com", "password": "faxter123", "expected": "failure"},
    {"email": "fermin@kidscorp.digital", "password": "wrongpassword", "expected": "failure"},
    {"email": "", "password": "", "expected": "failure"},
    {"email": "admin'; DROP TABLE users;--", "password": "any", "expected": "failure"},
    {"email": "fermin@kidscorp.digital", "password": "faxter123", "expected": "success"}
]

# Login Function to reuse login logic
def attempt_login(email, password):
    wait.until(ec.visibility_of_element_located((By.NAME, "email")))
    username = driver.find_element(By.NAME, "email")
    username.clear()
    username.send_keys(email)

    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(password)

    btnLogin = driver.find_element(By.XPATH, "//button[@type='submit']")
    btnLogin.click()

# Test Execution
for case in test_cases[:-1]:  # Skip the last test case for now
    attempt_login(case["email"], case["password"])
    try:
        if case["expected"] == "success":
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "logout_button")))
            print(f"Test passed for {case['email']}")
        else:
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "error")))
            print(f"Test passed for {case['email']}")
    except TimeoutException:
        print(f"Test failed for {case['email']}")

# Perform the last test case (success) separately
last_case = test_cases[-1]
attempt_login(last_case["email"], last_case["password"])
try:
    if last_case["expected"] == "success":
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "logout_button")))
        print(f"Test passed for {last_case['email']}")
    else:
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "error")))
        print(f"Test passed for {last_case['email']}")
except TimeoutException:
    print(f"Test failed for {last_case['email']}")

# Cleanup
driver.quit()
