import allure
import requests
from typing import Optional
from config.environment import Environment


def api_search_request(
        params: dict, token: Optional[str] = None
        ) -> requests.Response:
    """Выполняет API запрос для поиска.
        Args:
        params: Параметры запроса в виде словаря
        token: Токен авторизации (опционально)
        Returns:
        Ответ сервера в виде объекта Response
    """
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'

    with allure.step(
        f"Выполняем GET запрос с параметрами: {params}"
    ):
        response = requests.get(
            url=Environment.API_URL,
            params=params,
            headers=headers
        )
    return response
