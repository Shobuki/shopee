import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get('https://shopee.co.id/buyer/login?next=https%3A%2F%2Fshopee.co.id%2F')


def login():
    XPATH_username = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input'
    XPATH_password = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input'
    XPATH_login = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button'
    driver.find_element(By.XPATH, XPATH_username).send_keys('dagonzaalfredo@gmail.com')


    driver.find_element(By.XPATH, XPATH_password).send_keys('1B2c3a4b')
    time.sleep(2)

    driver.find_element(By.XPATH, XPATH_login).click()
    time.sleep(30)


def link():
    driver.get('https://shopee.co.id/cart')
    time.sleep(5)



# Call the login function
login()
link()

# Optionally, you can close the browser after you're done
# driver.quit()
