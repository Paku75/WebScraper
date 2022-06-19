from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://www.cuisineaz.com/categories/bases-cat48653")

try: 
    main = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "main"))
    )
    print(main.text)
    articles = main.find_element(by=By.TAG_NAME, value="article")
    # print(articles.text)
    # for offre in offres:
    #     header = offres.find_element(by=By.TAG_NAME, value="span")
    #     print(header.text)
finally:
    browser.quit()