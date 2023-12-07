# vim test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("http://83.5.245.147:5500/")
driver.implicitly_wait(1.0)
span1 = driver.find_element(By.CSS_SELECTOR, ".book-row > span:nth-child(1)")
span2 = driver.find_element(By.CSS_SELECTOR, ".book-row > span:nth-child(2)")
span3 = driver.find_element(By.CSS_SELECTOR, ".book-row > span:nth-child(3)")
if span1 == None or span2 == None or span3 == None:
    raise RuntimeError("UI isn't loaded correctly.")
if span1.text != 'a' or span2.text != 'b' or span3.text != 'c':
    raise RuntimeError("UI doesn't contain expected text.")

    # if span1 == "a" and span2 == "b" and span3 == "c":
    #     print("The book-row element has three spans next to each other with values: a, b, c")
    # else:
    #     raise Exception("The book-row element does not have three spans next to each other with values: a, b, c")

driver.quit()