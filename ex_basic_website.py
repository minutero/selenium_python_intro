#import Selenium
from selenium import webdriver

#Specific for this script
from pathlib import Path
import sys
from time import sleep

# Define some setup variables (Just use one of the 2)
#driver_path = Path(__file__).resolve().parent # Driver in the same folder as this file
driver_path = '/home/felipe/Proyectos/coffe_selenium' #Hardcoded path


chrome = webdriver.Chrome(str(driver_path) + r'/chromedriver') #change to the correct name of your file

#Navigate to the URL https://lambdatest.github.io/sample-todo-app/
chrome.get('https://lambdatest.github.io/sample-todo-app/')
chrome.maximize_window()
sleep(5)

#Select the first two checkboxes
chrome.find_element_by_name("li1").click()
chrome.find_element_by_name("li2").click()

#Checks that the page title matches "Sample page - lambdatest.com"
title = "Sample page - lambdatest.com"
assert title == chrome.title

#Send ‘Happy Testing at LambdaTest’ to the textbox with id = sampletodotext
sample_text = "Happy Testing at LambdaTest"
text_box = chrome.find_element_by_id("sampletodotext")
text_box.send_keys(sample_text)
sleep(2)

#Click the Add button
chrome.find_element_by_id("addbutton").click()
sleep(2)

#Verify whether the text has been added or not
output_str = chrome.find_element_by_name("li6").text
sys.stdout.write(output_str)    

#Close the browser after 2 seconds
sleep(2)
chrome.close()