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


path = "//*[@id='customer_login']/div[1]/form/p[4]/a"
lostPass = driver.find_element_by_xpath(path)
lostPass.click()
time.sleep(5)
username = "tegakoh202@ofenbuy.com"
casillaUser = driver.find_element_by_id("user_login")
casillaUser.clear()
casillaUser.send_keys(username)
boton = driver.find_element_by_xpath("//*[@id='post-9']/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/form/p[3]/button")
boton.click()