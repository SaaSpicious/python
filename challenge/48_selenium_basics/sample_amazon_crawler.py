from selenium import webdriver
from selenium.webdriver.common.by import By
REQUEST_URL="https://www.amazon.de/Hansgrohe-Pulsify-Select-Handdouche-Chroom/dp/B09S151KNJ/ref=sr_1_7"

#Configure the web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True) #Keep Browser open

driver = webdriver.Chrome(options=chrome_options)

# Easy Part: Open Page and get the price of a product through inspecting the price fields
driver.get(REQUEST_URL)
price_whole = driver.find_element(By.CLASS_NAME,"a-price-whole").text
price_fraction = driver.find_element(By.CLASS_NAME,"a-price-fraction").text
print(f"Price from the Amazon product: {price_whole},{price_fraction}")

# Intermediate: Access the attributes of a form field (in this case, the search bar) by the element name
search_bar = driver.find_element(By.NAME,value="field-keywords")
print(f"This element is of type: {search_bar.tag_name}")

# Searches an element by ID
search_button = driver.find_element(By.ID,value="nav-search-submit-button")
print(f"The size of the Search button is {search_button.size}")

# Search for a certain Element through CSS selector
product_title = driver.find_element(By.CSS_SELECTOR, value=".product-title-word-break")
print(f"The product title is: {product_title.text}")

# Searches for an element via XPATH
reseller = driver.find_element(By.XPATH, value='//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span')
print(f"The reseller is: {reseller.text}")

