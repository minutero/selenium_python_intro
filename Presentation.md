# <span style="color:green">[Selenium](https://www.selenium.dev/es/)</span>  
Selenium is a web-based automation testing framework. Its original purpose is utilizing web browsers to perform unit tests on your website’s functionalities, or checking of broken links and various other HTML assets.  

Selenium Webdriver is also a great tool for people to use in automating some of the monotonous web work that takes place on a regularly basis. 

## Use your preferred language
* Java
* [Python](https://selenium-python.readthedocs.io/)
* C#
* Ruby
* JavaScript

<br>

## What can you do with Selenium?

1. Automated web testing  
1. Downloading pictures/videos and uploading them to cloud storage or to social media  
1. Downloading web based reports  
1. Auto populate time sheets & trackers
1. Booking a Flight
1. Comparing prices


<br><br><br>

# <span style="color:lightblue">Usage</span>
## <span style="color:lightblue">1. Navigating</span>
    driver.get("http://www.google.com")
## <span style="color:lightblue">2. Finding an element</span>
    element = driver.find_element_by_id("passwd-id")
    element = driver.find_element_by_name("passwd")
    element = driver.find_element_by_xpath("//input[@id='passwd-id']")
    element = driver.find_element_by_css_selector("input#passwd-id")

More on finding elements [here](https://selenium-python.readthedocs.io/locating-elements.html)

## <span style="color:lightblue">3. Interacting with elements</span>
#### <span style="color:lightblue">Basic Interactions</span>
    element.send_keys(" and some", Keys.ARROW_DOWN)
    element.clear()
    element.click()

#### <span style="color:lightblue">Drag and Drop</span>
    element = driver.find_element_by_name("source")
    target = driver.find_element_by_name("target")

    from selenium.webdriver import ActionChains
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(element, target).perform()

#### <span style="color:lightblue">Scroll down</span>
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#### <span style="color:lightblue">Take Screenshot </span>
    driver.save_screenshot('screenshot.png') #If you don't specify a full path then is stored in the same folder as the driver