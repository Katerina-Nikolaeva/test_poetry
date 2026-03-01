import pytest

from src.decorators import log


# Тестируем простую функцию без ошибок
def test_decorators_log_success(capsys):
    @log()
    def simple_function():
        return "Success"

    simple_function()
    captured = capsys.readouterr()
    assert "FINISHED SUCCESSFULLY." in captured.out
    assert "RESULT: Success" in captured.out


# Тестируем логирование ошибки
def test_decorators_log_error(capsys):
    @log()
    def failing_function():
        raise ValueError("Something went wrong!")

    with pytest.raises(ValueError):
        failing_function()

    captured = capsys.readouterr()
    assert "ENDED WITH ERROR." in captured.out
    assert "TYPE OF ERROR: ValueError" in captured.out


# Тестируем логирование в файл
def test_decorators_log_to_file(tmp_path):
    logfile = tmp_path / "test_log.txt"

    @log(filename=str(logfile))
    def logged_function():
        return "Logged Success"

    logged_function()

    with open(logfile, "r") as f:
        content = f.read()
        assert "FINISHED SUCCESSFULLY." in content
        assert "RESULT: Logged Success" in content
