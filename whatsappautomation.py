from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


driver.get("https://web.whatsapp.com/")

input("Please Scan QR Code And Press Any Key to Continue: ")

BH = driver.find_element_by_css_selector('span[title="NAME"]')
BH.click()

testinput = driver.find_element_by_xpath("copy xpath of chat by using cntrl+shift+i")
testinput.send_keys("hiiii")
testinput.send_keys(Keys.RETURN)



