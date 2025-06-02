from selenium.webdriver.common.by import By
import time

def login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def test_logout(driver):
    login(driver)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)  # necessário para o menu abrir
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert "saucedemo.com" in driver.current_url
