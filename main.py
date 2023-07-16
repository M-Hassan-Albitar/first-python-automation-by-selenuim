from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")

time = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget ul time')
title = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget ul a')

events = {}
for e in range(len(time)):
    events.update({
        e: {
            "date": time[e].text,
            "title": title[e].text,
        }
    })

print(events)

driver.quit()
