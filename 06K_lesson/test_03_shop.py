from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def test_shop_purchase():
    """Тест покупки в интернет-магазине"""
    # Создаем опции для Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")  # Открыть на весь экран
    options.add_argument("--disable-notifications")  # Отключить уведомления

    # Создаем драйвер с опциями
    driver = webdriver.Firefox(options=options)

    try:
        # Открытие сайта магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        # Добавление товаров в корзину
        items = [
            'button[name="add-to-cart-sauce-labs-backpack"]',
            'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]',
            'button[name="add-to-cart-sauce-labs-onesie"]'
        ]
        for locator in items:
            item = driver.find_element(By.CSS_SELECTOR, locator)
            item.click()

        # Переход в корзину
        driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        # Заполнение формы
        driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, "#continue").click()

        # Ожидание загрузки страницы с итогом
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test="total-label"]'))
        )

        # Получаем итоговую сумму
        total_element = driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]')
        total_text = total_element.text

        # Извлекаем сумму
        total_match = re.search(r'\$\d+\.\d+', total_text)
        assert total_match, f"Не удалось найти сумму в тексте: {total_text}"
        total_value = total_match.group(0)

        # Проверка итоговой суммы
        expected_total = "$58.29"
        assert total_value == expected_total, f"Ожидалось {expected_total}, получено {total_value}"

        print(f"Тест пройден успешно! Итоговая сумма: {total_value}")

    finally:
        driver.quit()