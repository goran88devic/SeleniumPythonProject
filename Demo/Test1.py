import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://google.com")

element = driver.find_element_by_name("q")
element.send_keys("Automation step by step")
element.send_keys(Keys.ENTER)

#driver.find_element_by_name("q").send_keys("Automation step by step")
#driver.find_element_by_name("btnK").click()    - "btnk" element not interactable so we must use element access

time.sleep(10)
print(driver.title)
driver.close()
driver.quit()


print("Test complete")


