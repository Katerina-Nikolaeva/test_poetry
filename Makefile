# Запуск всех линтеров
lint: black isort flake8 mypy

# Запуск black
black:
	poetry run black .

# Запуск isort
isort:
	poetry run isort .

# Запуск flake8
flake8:
	poetry run flake8 .

# Запуск mypy
mypy:
	poetry run mypy .

# Очистка
clean:
	rm -rf .mypy_cache
	rm -rf __pycache__
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

.PHONY: lint black isort flake8 mypy clean
