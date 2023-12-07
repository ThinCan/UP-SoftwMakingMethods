from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Open the website
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://83.5.245.147:5500/")

# Fill the form
title = "title1"
description = "desc1"
author = "author1"

driver.find_element(By.ID, "book-form-input-title").send_keys(title)
driver.find_element(By.ID, "book-form-input-description").send_keys(description)
driver.find_element(By.ID, "book-form-input-author").send_keys(author)
driver.find_element(By.ID, "book-form-button-addbook").click()

# Check the child element
wait = WebDriverWait(driver, 10)
child = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#book-container > div")))
spans = child.find_elements(By.TAG_NAME, "span")

assert len(spans) == 3
assert spans[0].text == title
assert spans[1].text == description
assert spans[2].text == author

button = driver.find_element(By.CSS_SELECTOR, ".book-row button")
button.click()
wait = WebDriverWait(driver, 10)
update_inputs = driver.find_elements(By.CSS_SELECTOR, ".book-row input")
assert(len(update_inputs) == 3)
update_inputs[0].send_keys("1")
update_inputs[1].send_keys("2")
update_inputs[2].send_keys("3")

button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".book-row button:last-child")))
button.click()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(0.5)
spans = driver.find_elements(By.CSS_SELECTOR, ".book-row span")
assert len(spans) == 3
assert spans[0].text == "1"
assert spans[1].text == "2"
assert spans[2].text == "3"
# Find the last button inside #book-row and click it
button = driver.find_element(By.CSS_SELECTOR, ".book-row button:last-child")
button.click()

wait = WebDriverWait(driver, 10)
driver.implicitly_wait(1.5)
assert len(driver.find_elements(By.CSS_SELECTOR, "#book-container > *")) == 0
print("The test passed successfully!")
