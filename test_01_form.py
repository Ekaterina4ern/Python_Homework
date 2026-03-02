import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_default_edge_options():
    """Функция для создания опций Edge"""
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")  # Открыть на весь экран
    options.add_argument("--disable-notifications")  # Отключить уведомления
    options.add_argument("--disable-popup-blocking")  # Отключить блокировку всплывающих окон
    return options


@pytest.fixture
def driver():
    """Фикстура для браузера Edge с автоматической загрузкой драйвера"""
    try:
        # Пытаемся загрузить драйвер через webdriver-manager
        edge_service = EdgeService(EdgeChromiumDriverManager().install())
    except Exception as e:
        print(f"Ошибка при загрузке драйвера через webdriver-manager: {e}")
        print("Пробуем использовать драйвер из системного PATH...")
        # Если не получилось, пробуем без указания пути (драйвер должен быть в PATH)
        edge_service = EdgeService()

    # Получаем опции
    options = get_default_edge_options()

    # Создаем драйвер
    driver = webdriver.Edge(service=edge_service, options=options)
    yield driver
    driver.quit()


def test_fill_and_submit_form(driver):
    """Тест формы с проверкой подсветки полей"""
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")  # Оставляем пустым
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Нажатие кнопки Submit
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    # Ожидание появления результатов
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert"))
    )

    # Проверка, что поле Zip code подсвечено красным
    zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class"), \
        "Поле Zip code должно быть подсвечено красным"

    # Проверка, что остальные поля подсвечены зеленым
    green_highlighted_fields = driver.find_elements(By.CSS_SELECTOR, "div.alert.alert-success")
    assert len(green_highlighted_fields) == 9, \
        f"Найдено {len(green_highlighted_fields)} зеленых полей, а ожидалось 9"

    print("✓ Тест формы успешно пройден!")