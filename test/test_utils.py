import unittest
from unittest.mock import patch
from src.utils import load_and_convert_transactions


class TestLoadAndConvertTransactions(unittest.TestCase):
    @patch('builtins.open', create=True)
    def test_load_and_convert_transactions_valid_rub(self, mock_open):
        # Эмулируем открытие файла и содержание JSON
        mock_json_data = '''
        [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                }
            }
        ]
        '''
        mock_open.return_value.__enter__.return_value.read.return_value = mock_json_data

        # Выполняем функцию
        result = load_and_convert_transactions('data/operations.json')

        # Проверяем результат
        expected_result = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                }
            }
        ]
        self.assertEqual(result, expected_result)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open):
        # Выполняем функцию
        result = load_and_convert_transactions('data/operations.json')

        # Проверяем, что результат пустой
        self.assertEqual(result, [])

    @patch('builtins.open', create=True)
    def test_json_decode_error(self, mock_open):
        # Эмулируем открытие файла с некорректным JSON
        mock_open.return_value.__enter__.return_value.read.return_value = '{invalid json}'

        # Выполняем функцию
        result = load_and_convert_transactions('data/operations.json')

        # Проверяем, что результат пустой
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
