from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://fr.indeed.com/")
search = browser.find_element(by=By.ID, value="text-input-what")
search.send_keys("Developpeur")
search.send_keys(Keys.RETURN)

try: 
    main = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "resultsBody"))
    )
    offres = main.find_element(by=By.TAG_NAME, value="ul")
    print(offres.text)
    # for offre in offres:
    #     header = offres.find_element(by=By.TAG_NAME, value="span")
    #     print(header.text)
finally:
    browser.quit()