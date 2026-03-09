import unittest
from unittest.mock import patch
from src.external_api import get_exchange_rate, get_convert
from dotenv import load_dotenv
import os
import requests


class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.api_key = os.getenv("EXCHANGE_RATES_API_KEY")

    @patch("src.external_api.requests.get")
    def test_get_exchange_rate_valid_currencies(self, mock_get):
        # Подготавливаем ожидаемый ответ API
        mock_response = {
            "success": True,
            "timestamp": 1697044833,
            "base": "USD",
            "date": "2023-10-11",
            "rates": {"RUB": 90.55},
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

    @patch("src.external_api.requests.get")
    def test_get_exchange_rate_http_error(self, mock_get):
        # Эмулируем ошибку сервера
        mock_get.return_value.status_code = 400
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("Bad Request")

        with self.assertRaises(requests.exceptions.HTTPError):
            get_exchange_rate("ABC", "XYZ")

    def test_get_convert_rub_no_conversion_needed(self):
        # Тестируем случай, когда валюта уже рубли
        transaction = {"operationAmount": {"amount": "1000", "currency": {"name": "RUB", "code": "RUB"}}}
        result = get_convert(transaction)
        expected_result = 1000.0
        self.assertEqual(result, expected_result)

    @patch("src.external_api.requests.get")
    def test_get_convert_usd_to_rub(self, mock_get):
        # Эмулируем ответ API с готовой суммой конвертации
        mock_response = {"success": True, "result": 8500.0}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Транзакция в долларах
        transaction = {"operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}}}
        result = get_convert(transaction)
        expected_result = 8500.0
        self.assertEqual(result, expected_result)

    @patch("src.external_api.requests.get")
    def test_get_convert_eur_to_rub(self, mock_get):
        # Эмулируем ответ API с готовой суммой конвертации
        mock_response = {"success": True, "result": 4500.0}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Транзакция в евро
        transaction = {"operationAmount": {"amount": "50", "currency": {"name": "EUR", "code": "EUR"}}}
        result = get_convert(transaction)
        expected_result = 4500.0
        self.assertEqual(result, expected_result)

    def test_get_convert_unsupported_currency(self):
        # Тестируем исключение при неподдерживаемой валюте
        transaction = {"operationAmount": {"amount": "100", "currency": {"name": "GBP", "code": "GBP"}}}
        with self.assertRaises(ValueError):
            get_convert(transaction)


if __name__ == "__main__":
    unittest.main()
