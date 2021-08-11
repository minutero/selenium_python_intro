from pathlib import Path
from selenium import webdriver

download_path = '/home/felipe/Descargas/demo'

driver_path = Path(__file__).resolve().parent # Driver in the same folder as this file
#driver_path = '/home/felipe/Proyectos/coffe_selenium' #Hardcoded path

#Give some default options to Chrome so it downloads to a specific folder without asking
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : download_path}
chrome_options.add_experimental_option('prefs',prefs)
chrome = webdriver.Chrome(executable_path = str(driver_path) + r'/chromedriver', options=chrome_options) 

chrome.get('https://sites.google.com/a/chromium.org/chromedriver/downloads')

elem = chrome.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td[2]/div/div[3]/div/table/tbody/tr/td/div/div[4]/div[2]/div[3]/a')
assert 'ChromeDriver 92.0.4515.107' == elem.get_attribute("text")
elem.click()

chrome.get('https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_win32.zip')