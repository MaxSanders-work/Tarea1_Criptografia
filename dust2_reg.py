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

#Requiere input para registrarse
username = input("Ingrese mail para registrarse: ")
casillaUser = driver.find_element_by_id("reg_email")
casillaUser.clear()
casillaUser.send_keys(username)
casillaPassword = driver.find_element_by_id("reg_password")
casillaPassword.clear()
password = ''.join(random.choice(base) for j in range(10))
casillaPassword.send_keys(password)
print(password)
boton = driver.find_element_by_xpath("//*[@id= 'customer_login']/div[2]/form/p[3]/button")
boton.click()
