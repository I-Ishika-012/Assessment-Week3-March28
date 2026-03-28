"""
## Practical Exercise 1

### Title
**Automate Product Selection and Delivery Check on ShoppersStack**

### Description
Open the ShoppersStack website using Selenium WebDriver (https://www.shoppersstack.com/).

Automate the process of selecting a product category and verifying delivery availability using a pincode.

Perform the following steps:
- Launch the browser and open the ShoppersStack website
- Maximize the browser window
- Click on the **"APPLE"** product category
- Locate the delivery input field and enter the pincode
- Click on the **"Check"** button

Use appropriate locator strategies such as **XPath / ID / CSS Selectors** for identifying elements.
Implement synchronization using both **Implicit Wait** and **Explicit Wait**.

"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#chrome settings
opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

#maximising the window
driver.maximize_window()

#added implicit and explicit waits
driver.implicitly_wait(100)
wait = WebDriverWait(driver, 10)

#open shopperstack
driver.get("https://www.shoppersstack.com/")

#locating the req product using explicit wait
iphone = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='iphone']"))
)
iphone.click()

#locating the req element using explicit wait
# deliver = wait.until(
#     EC.presence_of_element_located((By.XPATH, "//input[id='Check Delivery']"))
# )

#locating the pincode field and input the pincode
deliver = driver.find_element(By.XPATH, "//input[@name='Check Delivery']")
deliver.send_keys("302022")

#locating check btn
check = driver.find_element(By.XPATH, "//button[@name='Check']")

#wait to click the check btn, click to check if its deliverable, for above pincode it's not :(
wait.until(EC.element_to_be_clickable(check)).click()

sleep(5)
driver.close()



