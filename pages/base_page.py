from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс Page Object для веб-страниц."""

    def __init__(self, driver: WebDriver):
        """Инициализация драйвера и ожиданий.
            Args:
            driver: Экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str):
        """Открывает указанный URL в браузере.
            Args:
            url: Адрес страницы для открытия.
        """
        self.driver.get(url)

    def search(self, text: str):
        """Выполняет поиск по тексту.
            Args:
            text: Текст для поиска.
        """
        locator = (By.CSS_SELECTOR, "input.search-input")
        search_input = self.wait.until(EC.presence_of_element_located(locator))
        search_input.clear()
        search_input.send_keys(text)
        search_input.submit()

    def enter_search_text(self, text: str):
        """Вводит текст в поле поиска без отправки.
            Args:
            text: Текст для ввода.
        """
        locator = (By.CSS_SELECTOR, "input.search-input")
        search_input = self.wait.until(EC.presence_of_element_located(locator))
        search_input.clear()
        search_input.send_keys(text)

    def has_search_results(self) -> bool:
        """Проверяет наличие результатов поиска.
            Returns:
            bool: True, если результаты есть.
        """
        try:
            locator = (By.CSS_SELECTOR, ".search-results .item")
            return len(self.wait.until(
                EC.presence_of_all_elements_located(locator)
                )) > 0
        except Exception:
            return False

    def has_empty_search_message(self) -> bool:
        """Проверяет сообщение о пустом поиске.
            Returns:
            bool: True, если сообщение отображается.
        """
        try:
            locator = (By.CSS_SELECTOR, ".empty-search-message")
            return self.wait.until(
                EC.presence_of_element_located(locator)
                ).is_displayed()
        except Exception:
            return False

    def has_error_message(self) -> bool:
        """Проверяет наличие сообщения об ошибке.
            Returns:
            bool: True, если ошибка отображается.
        """
        try:
            locator = (By.CSS_SELECTOR, ".error-message")
            return self.wait.until(
                EC.presence_of_element_located(locator)
                ).is_displayed()
        except Exception:
            return False

    def has_search_suggestions(self) -> bool:
        """Проверяет подсказки при поиске.
            Returns:
            bool: True, если подсказки есть.
        """
        try:
            locator = (By.CSS_SELECTOR, ".search-suggestions .item")
            return len(self.wait.until(
                EC.presence_of_all_elements_located(locator)
                )) > 0
        except Exception:
            return False

    def has_search_history(self) -> bool:
        """Проверяет историю поиска.
            Returns:
            bool: True, если история отображается.
        """
        try:
            locator = (By.CSS_SELECTOR, ".search-history .item")
            return len(self.wait.until(
                EC.presence_of_all_elements_located(locator)
                )) > 0
        except Exception:
            return False
