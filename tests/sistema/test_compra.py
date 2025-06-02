from selenium.webdriver.common.by import By
import time

def login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def test_adicionar_ao_carrinho(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    item_nome = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_nome == "Sauce Labs Backpack"

def test_finalizar_compra(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("João")
    driver.find_element(By.ID, "last-name").send_keys("Silva")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    msg = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "THANK YOU FOR YOUR ORDER" in msg
