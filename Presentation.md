# Selenium
Is a web-based automation testing framework. Its original purpose is utilizing web browsers to perform unit tests on your website’s functionalities, or checking of broken links and various other HTML assets.  
Selenium Webdriver is also a great tool for people to use in automating some of the monotonous web work that takes place on a regularly basis. 

<br>

For example:  
<span style="color:lightblue">1. Automated web testing  </span>  
<span style="color:lightblue">2. Downloading pictures/videos and uploading them to cloud storage or to social media  </span>   
<span style="color:lightblue">3. Downloading web based reports  </span>  
<span style="color:lightblue">4. Auto populate time sheets & trackers</span>
<span style="color:lightblue">5. Booking a Flight</span>


# Usage
## <span style="color:yellow">1. Navigating</span>
    driver.get("http://www.google.com")
## <span style="color:yellow">2. Interacting with the page</span>
### <span style="color:lightblue">2.1 Finding an element</span>
    element = driver.find_element_by_id("passwd-id")
    element = driver.find_element_by_name("passwd")
    element = driver.find_element_by_xpath("//input[@id='passwd-id']")
    element = driver.find_element_by_css_selector("input#passwd-id")

### <span style="color:lightblue">2.2 Basic interactions</span>
    element.send_keys(" and some", Keys.ARROW_DOWN)
    element.clear()
    element.click()

### <span style="color:lightblue">2.3 Other interactions</span>
This will find the first “SELECT” element on the page, and cycle through each of its OPTIONs in turn, printing out their values, and selecting each in turn.

    element = driver.find_element_by_xpath("//select[@name='name']")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        print("Value is: %s" % option.get_attribute("value"))
        option.click()

select = Select(driver.find_element_by_id('id'))
select.deselect_all()

