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

username = "rorife9895@smuvaj.com"
password = "EstoEsUnTest1"
casillaUser = driver.find_element_by_id("login-email")
casillaUser.clear()
casillaUser.send_keys(username)
casillaPassword = driver.find_element_by_id("login-password")
casillaPassword.clear()
casillaPassword.send_keys(password)
botton = driver.find_element_by_xpath("//*[@id='login-submit']/div")
botton.click()
cam = driver.find_element_by_xpath("//*[@id='password-section']/a")
cam.click()
curr = driver.find_elements_by_id("password-current")
curr.send_keys(password)
new = driver.find_elements_by_id("password")
new.send_keys("EstoEsUnTest2")
new2 = driver.find_elements_by_id("password-repeat")
new2.send_keys("EstoEsUnTest2")
camcon = driver.find_elements_by_xpath("//*[@id='changePassword-form']/fieldset/button/div")
camcon.click()