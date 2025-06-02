from selenium.webdriver.common.by import By
import time

def test_login_sucesso(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url

def test_login_falha(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.ID, "login-button").click()

    erro = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in erro or "do not match" in erro
    
def test_login_vazio(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "login-button").click()

    erro_usuario = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username is required" in erro_usuario

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "login-button").click()

    erro_senha = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Password is required" in erro_senha