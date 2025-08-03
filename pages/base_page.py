from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url: str):
        """Открывает указанный URL"""
        self.driver.get(url)
    
    def search(self, text: str):
        """Выполняет поиск по тексту"""
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        search_input.clear()
        search_input.send_keys(text)
        search_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        search_button.click()
    
    def enter_search_text(self, text: str):
        """Вводит текст в поле поиска без отправки"""
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        search_input.clear()
        search_input.send_keys(text)
    
    def has_search_results(self) -> bool:
        """Проверяет наличие результатов поиска"""
        try:
            return len(self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-card"))
            )) > 0
        except:
            return False
    
    def has_empty_search_message(self) -> bool:
        """Проверяет наличие сообщения о пустом поиске"""
        try:
            return self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".search-empty"))
            ).is_displayed()
        except:
            return False
    
    def has_error_message(self) -> bool:
        """Проверяет наличие сообщения об ошибке"""
        try:
            return self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".search-error"))
            ).is_displayed()
        except:
            return False
    
    def has_search_suggestions(self) -> bool:
        """Проверяет наличие подсказок поиска"""
        try:
            return len(self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".suggestions-item"))
            )) > 0
        except:
            return False
    
    def has_search_history(self) -> bool:
        """Проверяет наличие истории поиска"""
        try:
            return len(self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".history-item"))
            )) > 0
        except:
            return False
