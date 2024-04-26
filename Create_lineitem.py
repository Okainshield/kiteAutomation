import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


# Open the Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
driver.get('https://kite-qa2.kidscorp.digital/')
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
row_element = rows[3]  # Click on the fourth element (index 4)
row_element.click()
time.sleep(5)

# Click on the edit button of the campaign with specified text

# Find the <td> element with the specified text
td_element = driver.find_element(By.XPATH, "//td[contains(text(), '18018813725-Spin Master-Tech Deck-México-May')]")

# Navigate to Line-item page
element = driver.find_element(By.XPATH, "//div[@class='pdf_icon' and @title='View Line Items']")
element.click()
time.sleep(5)

# Click on Add New Line item
element = driver.find_element(By.XPATH, "//button[contains(text(), 'Add New Line Item')]")
element.click()
time.sleep(5)

# Fill the New Line-item form
# Fill Name for Line-item
input_element = driver.find_element(By.NAME, 'name')
input_element.click()
input_element.send_keys('Selenium Line-item')

# Select Inventory Type
inventory_type_dropdown = driver.find_element(By.NAME, "inventory_type_id")
inventory_type_dropdown.send_keys("Apps")  # Select "Apps" as an example

# Wait for the Format dropdown to become available
format_dropdown = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.NAME, "format_id"))
)

# Select the desired option from the Format dropdown
format_dropdown.send_keys("Pre Roll 30")  # Select "Pre Roll 30" as an example

# Find the dropdown element
dropdown = driver.find_element(By.NAME, "inversion_offer_type_id")
select = Select(dropdown)
# Select an option by visible text
select.select_by_visible_text("CPM")   # Replace "CPV" with the desired option

# Click on the start date input field to open the calendar
start_date_input = wait.until(ec.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Start Date')]/following-sibling::div//input")))
start_date_input.click()

# Wait for the calendar to be visible
calendar = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))

# Find and click on the given date
given_date = "26"  # Replace date accordingly
date_element = driver.find_element(By.XPATH, f"//div[contains(@class,'react-datepicker__day--0{given_date}') and not(contains(@class,'disabled'))]")
date_element.click()

# Click on the End date input field to open the calendar
End_date_input = wait.until(ec.element_to_be_clickable((By.XPATH, "//label[contains(text(),'End Date')]/following-sibling::div//input")))
End_date_input.click()

# Wait for the calendar to be visible
calendar = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))

# Find and click on the given date
given_date = "30"  # Replace '26' with the day of the given date
date_element = driver.find_element(By.XPATH, f"//div[contains(@class,'react-datepicker__day--0{given_date}') and not(contains(@class,'disabled'))]")
date_element.click()
time.sleep(3)

# Find the budget input field
budget_input = wait.until(ec.presence_of_element_located((By.NAME, "inversion_budget")))

# Clear any existing value and enter a new budget value
new_budget_value = 30000  # Set the new budget value
budget_input.send_keys(str(new_budget_value))

# Find the sell rate input field
sell_rate_input = wait.until(ec.presence_of_element_located((By.NAME, "inversion_sell_rate")))

# Clear any existing value and enter a new sell rate value
new_sell_rate_value = 25000  # Set the new sell rate value
sell_rate_input.clear()
sell_rate_input.send_keys(str(new_sell_rate_value))
time.sleep(3)

# Select Gender
wait = WebDriverWait(driver, 15)
# Find the ul element
ul_element = driver.find_element(By.CLASS_NAME, "optionContainer")

# Find all li elements within the ul element
li_elements = ul_element.find_elements(By.TAG_NAME, "li")

# Loop through the li elements to find and click the desired option
desired_option_text = "Mobile/Tablet"  # Change this to the option you want to select
for li_element in li_elements:
    if li_element.text.strip() == desired_option_text:
        li_element.click()
        break
time.sleep(5)


driver.quit()
