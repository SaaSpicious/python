from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
REQUEST_URL="https://en.wikipedia.org/wiki/Main_Page"

#Configure the web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True) #Keep Browser open

driver = webdriver.Chrome(options=chrome_options)
driver.get(REQUEST_URL)

# Find the amount of active editors in Wikipedia
article_stats = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
print(f"Active editors in Wikipedia: {article_stats.text}")

#Click the article
article_stats.click()

#Get back to the main page and find a link by text:
driver.get(REQUEST_URL)
more_articles = driver.find_element(By.LINK_TEXT, value="More featured articles")
more_articles.click()

#Get back to the main page and search for a keyword
driver.get(REQUEST_URL)
search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Käsekuchen")
search_bar.send_keys(Keys.ENTER) #Hitting Enter after typing!