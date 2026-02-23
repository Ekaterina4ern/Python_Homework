from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 30)

wait.until(
    EC.presence_of_element_located((By.ID, "text"))
)

wait.until(
    lambda driver: len(driver.find_elements(By.TAG_NAME, "img")) >= 4
)

images = driver.find_elements(By.TAG_NAME, "img")
for img in images[:3]:
    wait.until(
        lambda driver: img.get_attribute("src") and img.get_attribute("src") != ""
    )

images = driver.find_elements(By.TAG_NAME, "img")
src_value = images[2].get_attribute("src")
print(f"src 3-й картинки: {src_value}")