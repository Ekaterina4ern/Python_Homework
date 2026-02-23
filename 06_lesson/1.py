from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID, "ajaxButton")
button.click()

wait = WebDriverWait(driver, 15)

wait.until(EC.text_to_be_present_in_element(
    (By.ID, "content"),
    "Data loaded with AJAX get request."
))

green_banner = driver.find_element(By.CSS_SELECTOR, "p.bg-success")
text = green_banner.text

print(text)
