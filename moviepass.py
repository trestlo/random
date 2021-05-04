### This automation would open support tickets at MoviePass since they began ignoring requests and continued to charge
### people's accounts while they attempted to figure out how to stop losing money.

### Note: They didn't figure it out. RIP Moviepass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.implicitly_wait(30)

# Navigate to the support page and open the case
driver.get("https://moviepass.zendesk.com/hc/en-us/requests/new")
boxes = driver.find_elements_by_xpath("(//input[contains(@id, 'request_anonymous')])")

# Input account info
boxes[0].send_keys("leo.pineiro@outlook.com")
boxes = driver.find_elements_by_xpath("(//input[contains(@id, 'request_custom')])")
boxes[1].send_keys("Aurelio Pineiro")
boxes[2].send_keys("5947")

inputs = driver.find_elements_by_class_name("nesty-input")
inputs[0].click()
first = inputs[0]
second = inputs[1]

# Click through the support page selecting the case reason
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(first, 0, 0)
action.click()
action.perform()

action.move_to_element_with_offset(first, 10, 50)
action.click()
action.perform()

driver.execute_script("window.scrollTo(0, 200)") 

action = webdriver.common.action_chains.ActionChains(driver)
second.click()
action.move_to_element_with_offset(second, 30, 50)
action.click()
action.perform()

# Fill in the details
driver.find_element_by_id("request_subject").send_keys("Link in gift activation email does not work")
driver.find_element_by_id("request_description").send_keys("Please respond to one of our hundreds of support tickets. We are unable to activate our cards due to the dead links sent in emails.")

# This opens the case
driver.find_element_by_name("commit").click()

driver.quit()
