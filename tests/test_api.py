import allure
import pytest
from config.environment import Environment
from config.test_data import TestData
from utils.helpers import api_search_request


@allure.feature("API Тесты")
@allure.story("Поиск книг")
class TestSearchAPI:
    @pytest.mark.parametrize(
        "phrase_type",
        ['cyrillic', 'latin', 'with_numbers']
    )
    def test_positive_search(self, phrase_type: str):
        """Позитивные тесты поиска по разным типам названий."""
        params = {
            'customerCityId': Environment.DEFAULT_CITY_ID,
            'phrase': TestData.VALID_PHRASES[phrase_type]
        }

        with allure.step(
            f"Поиск по фразе: {TestData.VALID_PHRASES[phrase_type]}"
        ):
            response = api_search_request(params)

        assert response.status_code == 200, (
            f"Ожидался код 200, получен {response.status_code}"
        )
        assert len(response.json()) > 0, (
            "Результаты поиска не должны быть пустыми"
        )

    def test_search_with_invalid_token(self):
        """Тест поиска с невалидным токеном."""
        params = {
            'customerCityId': Environment.DEFAULT_CITY_ID,
            'phrase': TestData.VALID_PHRASES['cyrillic']
        }

        with allure.step("Поиск с невалидным токеном"):
            response = api_search_request(
                params, token=TestData.INVALID_TOKENS[0]
                )

        assert response.status_code == 401, (
            f"Ожидался код 401, получен {response.status_code}"
        )

    @pytest.mark.parametrize(
        "phrase_type",
        ['random_chars', 'emojis']
    )
    def test_negative_search(self, phrase_type: str):
        """Негативные тесты поиска."""
        params = {
            'customerCityId': Environment.DEFAULT_CITY_ID,
            'phrase': TestData.INVALID_PHRASES[phrase_type]
        }

        expected_status = 422 if phrase_type == 'emojis' else 200

        with allure.step(
            f"Поиск по невалид. фразе: {TestData.INVALID_PHRASES[phrase_type]}"
        ):
            response = api_search_request(params)

        assert response.status_code == expected_status, (
            f"Ожидался код {expected_status}, получен {response.status_code}"
        )
