import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from config.environment import Environment
from config.test_data import TestData
from pages.base_page import BasePage


@allure.feature("UI Тесты")
@allure.story("Поиск книг")
class TestSearchUI:

    def test_valid_search(self, driver: WebDriver):
        """Тест UI поиска по валидным фразам."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.search("Мастер и Мартгарита")
        assert page.has_search_results(), "Не найдены результаты поиска"

    def test_special_chars_search(self, driver: WebDriver):
        """Тест поиска со спецсимволами."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.search("№№№№№#######++++++~~~~~")
        assert page.has_not_found_message(), "Не найдено сообщение об ошибке"

    def test_search_suggestions(self, driver: WebDriver):
        """Тест подсказок при поиске."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.enter_search_text("Мастер и Маргарита")
        assert page.has_search_suggestions(), "Не найдены подсказки поиска"

    def test_catalog_filter(self, driver: WebDriver):
        """Тест истории поиска."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.search("Мастер и Маргарита")
        page.open(Environment.BASE_URL)
        assert page.has_catalog_filters, "Не найден фильтр каталогов"

    def test_filter_status(self, driver: WebDriver):
        """Тест истории поиска."""
        page = BasePage(driver)
        page.open(Environment.BASE_URL)
        page.search("Мастер и Маргарита")
        page.open(Environment.BASE_URL)
        assert page.has_filter_status, "Не найден фильтр"
