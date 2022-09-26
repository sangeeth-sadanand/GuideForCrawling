# Selenium

Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver.

## Installation

``` bash
pip install selenium
```

Download the drivers and place the driver in path. 

The driver can be placed in the work folder or a common driver can be used for multiple scripts. If the driver is not placed in the work folder driver should be added in the path for the windows folders. 

## Import and start driver

``` python
from selenium import webdriver

driver = webdriver.Firefox()
# OR
driver = webdriver.Chrome()
```

## To request page

``` python
driver.get(url)
```

## Navigating

The first thing you'll want to do with WebDriver is navigate to a link. The normal way to do this is by calling get method

``` python
driver.get("http://www.google.com")
```

### Interacting with the page

``` python
<input type="text" name="passwd" id="passwd-id" />
```

This element can be accessed by all the following methods

``` python
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
element = driver.find_element_by_css_selector("input#passwd-id")
```

### To send a key

``` python
from selenium.webdriver.common.keys import Keys

element.send_keys("some text")

element.send_keys(" and some", Keys.ARROW_DOWN)

element.clear()
```

### Select option

``` python
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_name('name'))

select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
select.deselect_all()
```

### Submit the form

``` python
driver.find_element_by_id("submit").click()or element.submit()# element can be any method in the form
```

### Drag and drop

``` python
from selenium.webdriver import ActionChainselement = driver.find_element_by_name("source")target = driver.find_element_by_name("target")action_chains = ActionChains(driver)action_chains.drag_and_drop(element, target).perform()
```

### Moving between windows and frames

``` python
driver.switch_to_window("windowName")for handle in driver.window_handles:    driver.switch_to_window(handle)
```

To switch between frames

``` python
driver.switch_to_frame("frameName")# ordriver.switch_to_frame("frameName.0.child")
```

### popup dialog

``` python
alert = driver.switch_to.alert
```

### history and location

``` python
driver.forward()driver.back()
```

### Cookies

``` python
# Go to the correct domain
driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain

cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}

driver.add_cookie(cookie)

# And now output all the available cookies for the current URL

driver.get_cookies()
```

## Locating Elements

Selenium provides the following methods to locate elements in a page:

-   find_element_by_id
-   find_element_by_name
-   find_element_by_xpath
-   find_element_by_link_text
-   find_element_by_partial_link_text
-   find_element_by_tag_name
-   find_element_by_class_name
-   find_element_by_css_selector

To find multiple elements (these methods will return a list):

-   find_elements_by_name
-   find_elements_by_xpath
-   find_elements_by_link_text
-   find_elements_by_partial_link_text
-   find_elements_by_tag_name
-   find_elements_by_class_name
-   find_elements_by_css_selector

``` python
from selenium.webdriver.common.by 
import Bydriver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```

These are the attributes available for By class:

``` python
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

## Waits

When a page is loaded by the browser, the elements within that page may load at different time intervals. This makes locating elements difficult: if an element is not yet present in the DOM, a locate function will raise an ElementNotVisibleException exception.

### Implicit Waits

An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available.

``` python
from selenium import webdriver

driver = webdriver.Firefox()driver.implicitly_wait(10) # seconds

driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```

### Explicit Waits

An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.

``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("http://somedomain/url_that_delays_loading")
try:    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:    
    driver.quit()
```

## Expected Conditions

There are some common conditions that are frequently of use when automating web browsers. Listed below are the names of each. Selenium Python binding provides some convenience methods so you don't have to code an expected_condition class yourself or create your own utility package for them.

-   title_is
-   title_contains
-   presence_of_element_located
-   visibility_of_element_located
-   visibility_of
-   presence_of_all_elements_located
-   text_to_be_present_in_element
-   text_to_be_present_in_element_value
-   frame_to_be_available_and_switch_to_it
-   invisibility_of_element_located
-   element_to_be_clickable
-   staleness_of
-   element_to_be_selected
-   element_located_to_be_selected
-   element_selection_state_to_be
-   element_located_selection_state_to_be
-   alert_is_present

``` python
from selenium.webdriver.support import expected_conditions as ECwait = WebDriverWait(driver, 10)element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
```

