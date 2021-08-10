#import packages
from selenium import webdriver
from pathlib import Path
import sys
from time import sleep

# Define some setup variables (Just use one of the 2)
driver_path = Path(__file__).resolve().parent # Driver in the same folder as this file
#driver_path = '/home/felipe/Proyectos/coffe_selenium' #Hardcoded path


driver = webdriver.Chrome(str(driver_path) + r'/chromedriver') #change to the correct name of your file

#Navigate to the URL https://lambdatest.github.io/sample-todo-app/
driver.get('https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select')
driver.maximize_window()
sleep(5)

driver.execute_script("window.scrollTo(0, 4050)")
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_xpath('/html/body/select'))
select.deselect_all()