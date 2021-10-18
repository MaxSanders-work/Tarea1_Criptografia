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

username = "tegakoh202@ofenbuy.com"
a = driver.find_element_by_id("forgot-password")
a.click()
mail = driver.find_element_by_id("email")
mail.send_keys(username)
botton = driver.find_element_by_xpath("//*[@id='requestPasswordChange-form']/fieldset/button/div")
botton.click()