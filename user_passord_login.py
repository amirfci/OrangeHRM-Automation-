import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def user_Pass_Check():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    username.send_keys("admin")
    password.send_keys("admin123")
    button.click()
    time.sleep(5)
    driver.close()

user_Pass_Check()
