from selenium import webdriver
from selenium.webdriver.common.keys import Keys #The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from pathlib import Path
from time import sleep

driver_path = Path(__file__).resolve().parent #Driver in the same folder as this file
chrome = webdriver.Chrome(str(driver_path) + r'/chromedriver') #change to the correct name of your file

chrome.get("http://www.python.org")
assert "Python" in chrome.title
sleep(2)

elem = chrome.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon",Keys.RETURN)

assert "No results found." not in chrome.page_source

sleep(5)
chrome.close()

