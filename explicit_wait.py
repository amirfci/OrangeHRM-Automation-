from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def user_Pass_Check():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    try:
        username = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='username']")))
        username.send_keys("admin")
    except Exception as e:
        print("Exception Type: ",type(e).__name__)
    password = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='password'")))
    button =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".orangehrm-login-button")))

    password.send_keys("admin123")
    button.click()

user_Pass_Check()