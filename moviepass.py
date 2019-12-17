### This automation would open support tickets at MoviePass since they began ignoring requests and continued to charge
### people's accounts while they attempted to figure out how to stop losing money.

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
driver.find_element_by_id("request_description").send_keys("I received and email about receiving a gift of Moviepass. A couple of weeks later I received the card, but when I click on the link in the email to claim my gift I get a page that says: \'Please Fix the following errors. Your Gift Wasn't Found. Please Contact Customer Service.\' After two months of attempting to contact you (while my friend still gets charged every month), I have still not received a resolution. Just to go over the details: I have the card, I don't have a working moviepass account. Resetting my password just leads to another invalid credentials email. Please take a look at this issue.")

# This opens the case
driver.find_element_by_name("commit").click()

driver.quit()
