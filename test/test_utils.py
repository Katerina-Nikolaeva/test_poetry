import unittest
import os
import tempfile
import json
from src.utils import load_and_convert_transactions


class TestLoadAndConvertTransactions(unittest.TestCase):
    def setUp(self):
        # Создание временного файла с корректными данными
        self.test_file_correct = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        correct_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        json.dump(correct_data, self.test_file_correct)
        self.test_file_correct.close()

        # Создание временного файла с неправильными данными (несписок)
        self.test_file_incorrect = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        incorrect_data = {"key": "value"}  # Некорректные данные (не список)
        json.dump(incorrect_data, self.test_file_incorrect)
        self.test_file_incorrect.close()

    def tearDown(self):
        # Удаляем временные файлы после завершения тестов
        os.remove(self.test_file_correct.name)
        os.remove(self.test_file_incorrect.name)

    def test_load_and_convert_transactions_correct_file(self):
        # Тестируем чтение корректного файла
        result = load_and_convert_transactions(self.test_file_correct.name)
        expected_result = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        self.assertEqual(result, expected_result)

    def test_load_and_convert_transactions_incorrect_format(self):
        # Тестируем чтение файла с неправильным форматом (не список)
        result = load_and_convert_transactions(self.test_file_incorrect.name)
        self.assertEqual(result, [])

    def test_load_and_convert_transactions_nonexistent_file(self):
        # Тестируем попытку прочитать несуществующий файл
        non_existent_file = "/nonexistent/path/to/file.json"
        result = load_and_convert_transactions(non_existent_file)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
