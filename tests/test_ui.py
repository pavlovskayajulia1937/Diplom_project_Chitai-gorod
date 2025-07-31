import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from config.environment import Environment
from config.test_data import TestData
from pages.base_page import BasePage


@allure.feature("UI Тесты")
@allure.story("Поиск книг")
class TestSearchUI:
    @pytest.mark.parametrize(
        "phrase",
        TestData.VALID_PHRASES.values()
    )
    def test_valid_search(self, driver: WebDriver, phrase: str):
        """Тест UI поиска по валидным фразам."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.search(phrase)
        assert page.has_search_results(), "Не найдены результаты поиска"

    def test_empty_search(self, driver: WebDriver):
        """Тест поиска без ввода фразы."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.search("")
        assert page.has_empty_search_message(), (
            "Не найдено сообщение о пустом поиске"
        )

    def test_special_chars_search(self, driver: WebDriver):
        """Тест поиска со спецсимволами."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.search(TestData.INVALID_PHRASES['emojis'])
        assert page.has_error_message(), "Не найдено сообщение об ошибке"

    def test_search_suggestions(self, driver: WebDriver):
        """Тест подсказок при поиске."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.enter_search_text(TestData.VALID_PHRASES['cyrillic'][:3])
        assert page.has_search_suggestions(), "Не найдены подсказки поиска"

    def test_search_history(self, driver: WebDriver):
        """Тест истории поиска."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.search(TestData.VALID_PHRASES['cyrillic'])
        page.open(Environment.BASE_URL)
        assert page.has_search_history(), "Не найдена история поиска"
