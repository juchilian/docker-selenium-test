from time import sleep
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

sleep(5)

driver = webdriver.Remote('http://selenium:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.CHROME)

driver.get("https://python.org")

print(driver.title)
# driver.save_screenshot('screenshot.png')
