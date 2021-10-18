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

boton = driver.find_element_by_id("didomi-notice-agree-button")
boton.click()
time.sleep(5)

username = input("Ingrese mail para registrarse: ")
crearcuenta = driver.find_element_by_xpath("//*[@id='fusion-app']/main/div/div[2]/div/a")
crearcuenta.click()
casillaUser = driver.find_element_by_id("register-email")
casillaUser.clear()
casillaUser.send_keys(username)
casillaPassword = driver.find_element_by_id("register-password")
casillaPassword.clear()
password = ''.join(random.choice(base) for j in range(10))
casillaPassword.send_keys(password)
print(password)
cap = driver.find_element_by_xpath("//*[@id='recaptcha-anchor']/div[1]")
cap.click()
condi = driver.find_element_by_id("tos")
condi.click()
botton = driver.find_element_by_id("register-submit")
botton.click()