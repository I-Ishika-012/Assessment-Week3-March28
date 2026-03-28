"""
## Practical Exercise 2

### Title
**Automate Myntra Product Selection**

### Description
Open the Myntra website using Selenium WebDriver (https://www.myntra.com/).

Automate the process of navigating categories, selecting a product, applying filters, sorting products and adding to bag.

Perform the following steps:
- Launch the browser and open the Myntra website
- Maximize the browser window
- Hover over the **Genz** category
- Click on **"Jackets Under ₹899"**
- Select any 2 filter under the product filters (e.g., brand, size, or color)
- Click on the **Sort By** 'Popularity'
- Click on the any one product
- Select size (if mentioned)
- Add to bag
Use appropriate locator strategies such as **XPath / CSS Selectors** and implement **ActionChains** for hovering and clicking.
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#browser settings
opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)

#maximize window
driver.maximize_window()

#explicit wait instance
wait = WebDriverWait(driver, 20)

#action instance
action = ActionChains(driver)

driver.get("https://www.myntra.com/")

sleep(3)

#locating genz category
genz = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Genz']")))
action.move_to_element(genz).perform()

#locating Jackets Under ₹899 under genz
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Jackets Under ₹899')]"))).click()

#waiting until filters are visible
filters = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "common-customCheckbox")))
filters[1].click()
filters[3].click()

#select/click sort by
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Sort by')]"))).click()
#choose popularity
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Popularity')]"))).click()

#selecting a certain product out of the product base
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-base"))).click()

#change window to product page
driver.switch_to.window(driver.window_handles[1])

#select jacket size
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "size-buttons-size-button"))).click()

#add to cart!
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='ADD TO BAG']"))).click()

sleep(10)
driver.quit()