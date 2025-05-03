from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

REQUEST_URL="https://orteil.dashnet.org/experiments/cookie/"

def check_buyables(driver):
    elements = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    highest_price = 0
    best_item = None
    for element in elements:
        if element.get_attribute("class") == "grayed":
            pass
        elif len(element.text) > 2:
            try:
                element_price = int( #Convert Result to in)
                    str(element.text)
                    .split(" - ")[1] #First choose everything behind the dash
                    .split("\n")[0] # then everything before the line break
                )
            except:
                print(f"Error in text parsing: {element.text}")
            if element_price > highest_price:
                highest_price = element_price
                best_item = element
        else:
            pass #ignore near-empty elements
    if best_item: #only click, if an item was found to click!
        best_item.click()


#Configure the web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True) #Keep Browser open

driver = webdriver.Chrome(options=chrome_options)
driver.get(REQUEST_URL)

cookie = driver.find_element(By.ID, value="cookie")

target_time=time() + 60*5 # run for 5 minutes
five_seconds=time() + 5 # set timer for 5 seconds

while time() < target_time:
    pass
    cookie.click()
    if time() >= five_seconds:
        check_buyables(driver)
        five_seconds = time() + 5  # reset timer