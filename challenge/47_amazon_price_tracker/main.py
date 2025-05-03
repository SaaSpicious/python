from bs4 import BeautifulSoup
import lxml
import requests

#REQUEST_URL="https://appbrewery.github.io/instant_pot/"
REQUEST_URL="https://www.amazon.de/Hansgrohe-Pulsify-Select-Handdouche-Chroom/dp/B09S151KNJ/ref=sr_1_7"

def get_sample_page(request_url):
    # Download the web page
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
              "Accept-Language": "en-US"}
    webpage = requests.get(url=request_url,headers=header).text

    # Create BS4 out of the response.
    content = BeautifulSoup(webpage,"html.parser")

    return content


def get_price(soup):
    price_whole = int(soup.find(class_="a-price-whole")
                      .getText()
                      .split(",")[0]
                      )
    price_fraction = int(soup.find(class_="a-price-fraction").getText())
    price = price_whole + price_fraction / 100
    return price


soup = get_sample_page(REQUEST_URL)
print(get_price(soup))