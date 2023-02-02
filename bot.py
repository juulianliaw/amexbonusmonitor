from selenium import webdriver
from selenium.webdriver.support.select import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "https://www.singaporeair.com/en_UK/us/home#/book/bookflight"
username = "jasonsjoints69@gmail.com"
password = "ToppestoftheG69"
driver = webdriver.Chrome("/Users/julianliaw/Downloads/chromedriver")
actions = ActionChains(driver) 

driver.get(url)
driver.find_element(By.XPATH, '//*[@id="redeemFlights"]').click()
driver.find_element(By.XPATH, '//*[@id="userEmailKfPpsClub"]').send_keys(username)
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="userPasswordKfPpsClub"]').send_keys(password)
actions.send_keys(Keys.ENTER)
actions.perform()

#driver.find_element(By.XPATH, '//*[@id="header"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="redeemFlights"]').click()

#input origin airport (SIN for now)
driver.find_element(By.XPATH, '//*[@id="flightOrigin2"]').send_keys("SIN")
driver.find_element(By.XPATH, '//*[@id="hwidget"]/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/form/div[1]/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="redeemFlightDestination"]').send_keys("NAR".RETURN)





