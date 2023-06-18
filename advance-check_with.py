from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def user_Pass_Check(username,password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    try:
        username_field = WebDriverWait(driver,10,poll_frequency=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='username']")))
        try:
            assert username_field.is_enabled(), f"username field Disabled."
            username_field.send_keys(username)
            print("Username is enabled")

        except Exception as e:
            print("username is error")

    except Exception as e:
           print("Exception Type: ",type(e).__name__)
    try:
        password_field = WebDriverWait(driver,15,poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='password'")))
        try:
            assert password_field.is_enabled(),f"Password field is disabled."
            password_field.send_keys(password)
            print("password field is enabled")
        except Exception as e:
            print("password is error")
    except Exception as e:
        print("Exception Type: ",type(e).__name__)
    try:
       button =WebDriverWait(driver,10,poll_frequency=2).until(
           EC.visibility_of_element_located((By.CSS_SELECTOR,".orangehrm-login-button")))

       button.click()
       print("login success")
    except Exception as e:
        print("Exception Type:",type(e).__name__)

user_Pass_Check("admin","admin123")