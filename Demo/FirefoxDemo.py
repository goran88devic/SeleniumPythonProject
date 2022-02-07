from datetime import time

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = "../drivers/geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)

driver.get("https://google.com")
element = driver.find_element_by_name("q")
element.send_keys("Automation step by step")
element.send_keys(Keys.ENTER)
#driver.find_element_by_name("q").send_keys("Automation step by step")
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

print(driver.title)


time.sleep(10)

driver.close()
driver.quit()

print("test complete")