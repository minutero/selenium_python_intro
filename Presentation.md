# <span style="color:lightblue">Pillars</span>
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