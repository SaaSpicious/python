from selenium import webdriver
from selenium.webdriver.common.by import By
REQUEST_URL="https://www.python.org"

#Configure the web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True) #Keep Browser open

driver = webdriver.Chrome(options=chrome_options)
driver.get(REQUEST_URL)

# Find all events with names and dates on the python.org website
elements = driver.find_elements(By.CSS_SELECTOR, value="div.list-widgets.row div.medium-widget.event-widget.last div ul li")
events = {}
for i in range(len(elements)):
    text = elements[i].text
    text_elements = text.split("\n")
    events[i]={
            "time": text_elements[0],
            "name": text_elements[1],
        }

print(events)


    # content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child(1)