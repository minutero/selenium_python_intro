import getpass as gt
import base64
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.action_chains import ActionChains

#username = gt.getuser() #If you want to get the user from the session
username = input('Username: ')
password = base64.b64encode(gt.getpass(prompt='Password: ', stream=None).encode('utf8'))

driver_path = Path(__file__).resolve().parent # Driver in the same folder as this file
#driver_path = '/home/felipe/Proyectos/coffe_selenium' #Hardcoded path

chrome = webdriver.Chrome(str(driver_path) + r'/chromedriver') #change to the correct name of your file

chrome.get('https://es-la.facebook.com/')

input_user = chrome.find_element_by_id('email')
input_user.clear()
input_user.send_keys(username)

#First Option to enter password with ActionChains
#In this case you don't need to identify the element for password,
# but instead you perform actions from your last know point
actions = ActionChains(chrome)
actions.send_keys(Keys.TAB)
actions.send_keys(base64.b64decode(password).decode("utf8"))
actions.send_keys(Keys.ENTER)
actions.perform()

#Second option with find_element 
#You identify the specific element for password and send the corresponding keys
input_pass = chrome.find_element_by_id('pass')
input_pass.clear()
input_pass.send_keys(base64.b64decode(password).decode("utf8"), Keys.ENTER)