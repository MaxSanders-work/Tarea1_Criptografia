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

username = "rorife9895@smuvaj.com"
password = "EstoEsUnTest1"
casillaUser = driver.find_element_by_id("username")
casillaUser.clear()
casillaUser.send_keys(username)
casillaPassword = driver.find_element_by_id("password")
casillaPassword.clear()
casillaPassword.send_keys(password)
boton = driver.find_element_by_xpath("//*[@id='customer_login']/div[1]/form/p[3]/button")
boton.click()


detalles = driver.find_element_by_xpath("//*[@id='post-9']/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/nav/ul/li[4]/a")
detalles.click()


nombre = driver.find_element_by_id("account_first_name")
nombre.clear()
nombre.send_keys("Jhon")
apellido = driver.find_element_by_id("account_last_name")
apellido.clear()
apellido.send_keys("Doe")
currPass = driver.find_element_by_id("password_current")
currPass.clear()
currPass.send_keys(password)
newPass = driver.find_element_by_id("password_1")
newPass.clear()
newPass.send_keys("EstoEsUnTest2")
repNewPass = driver.find_element_by_id("password_2")
repNewPass.clear()
repNewPass.send_keys("EstoEsUnTest2")
boton = driver.find_element_by_xpath("//*[@id='post-9']/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/form/p[5]/button")
boton.click()