import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TEST_URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome()

driver.get(TEST_URL)

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Mo")
first_name.send_keys(Keys.TAB)

last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Hassan")
last_name.send_keys(Keys.TAB)

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("codermhassan@gmail.com")
email.send_keys(Keys.TAB)

sign_up = driver.find_element(by=By.TAG_NAME, value="button")
sign_up.click()

time.sleep(5)

driver.quit()



# URL = "https://en.wikipedia.org/wiki/Main_Page"
#
# driver = webdriver.Chrome()
#
# driver.get(URL)
#
# # articles_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount > a:nth-child(1)")
# #
# # print(articles_count.text)
#
# driver.quit()
