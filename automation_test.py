from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Function to verify login functionality
def verify_login():
    # Open the login page
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Wait for the username field to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-v-1f99f73c][name="username"]')))
    
    # Find username and password fields and login button
    username_field = driver.find_element(By.CSS_SELECTOR, '[data-v-1f99f73c][name="username"]')
    password_field = driver.find_element(By.CSS_SELECTOR, '[data-v-1f99f73c][name="password"]')
    login_button = driver.find_element(By.CSS_SELECTOR, '[data-v-10d463b7][type="submit"]')
    
    # Enter valid credentials
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    
    # Click the login button
    login_button.click()
    
    # Verify login by checking if dashboard is loaded
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menu_dashboard_index")))
        dashboard_element = driver.find_element(By.ID, "menu_dashboard_index")
        if dashboard_element.is_displayed():
            print("Login Test Passed")
        else:
            print("Login Test Failed")
    except:
        print("Login Test Failed")

    driver.quit()

# Run the login test case
verify_login()
