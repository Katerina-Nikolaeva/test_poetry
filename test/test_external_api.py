import requests
import unittest
from unittest.mock import patch, MagicMock
from src.external_api import fetch_exchange_rate


class TestFetchExchangeRate(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_exchange_rate_successful(self, mock_get):
        # Эмулируем успешный ответ от API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'success': True,
            'quotes': {
                'USDRUB': 70.0
            }
        }
        mock_get.return_value = mock_response

        # Выполняем функцию
        result = fetch_exchange_rate('RUB', 'USD')

        # Проверяем результат
        self.assertEqual(result, 70.0)

    @patch('requests.get')
    def test_fetch_exchange_rate_api_error(self, mock_get):
        # Эмулируем ошибку API (например, 500 Internal Server Error)
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Internal Server Error")
        mock_get.return_value = mock_response

        # Выполняем функцию
        with self.assertRaises(requests.exceptions.HTTPError):
            fetch_exchange_rate('RUB', 'USD')

    @patch('requests.get')
    def test_fetch_exchange_rate_missed_data(self, mock_get):
        # Эмулируем ответ API без нужного курса
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'success': True,
            'quotes': {}
        }
        mock_get.return_value = mock_response

        # Выполняем функцию
        result = fetch_exchange_rate('RUB', 'USD')

        # Проверяем результат (ничего не найдено)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
