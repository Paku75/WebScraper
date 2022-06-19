from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://jobs-stages.letudiant.fr/")
search = browser.find_element(by=By.ID, value="search")
search.send_keys("Conseiller")
search.send_keys(Keys.RETURN)

try: 
    main = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tw-main-container tw-bg-white"))
    )
    offres = main.find_element(by=By.CLASS_NAME, value="sm:tw--mx-3 tw--mx-1 tw--mb-2 sm:tw--mb-6")
    print(offres.text)
    # for offre in offres:
    #     header = offres.find_element(by=By.TAG_NAME, value="span")
    #     print(header.text)
finally:
    browser.quit()