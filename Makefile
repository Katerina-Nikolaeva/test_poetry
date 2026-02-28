all: lint tests coverage

# Запуск всех линтеров
lint: black isort flake8 mypy

# Запуск black
black:
	@echo
	@echo "-> Run black..."
	@poetry run black .

# Запуск isort
isort:
	@echo
	@echo "-> Run isort..."
	@poetry run isort .

# Запуск flake8
flake8:
	@echo
	@echo "-> Run flake8..."
	@poetry run flake8 .

# Запуск mypy
mypy:
	@echo
	@echo "-> Run mypy..."
	@poetry run mypy .

tests:
	@echo
	@echo "-> Run tests..."
	@pytest

coverage:
	@echo
	@echo "-> Check tests coverage..."
	@poetry run pytest --cov

coverage-open: coverage
	@echo
	@echo "-> Open tests coverage..."
	@open htmlcov/index.html

# Очистка
clean:
	@echo
	@echo "-> Clean up..."
	rm -rf .mypy_cache
	rm -rf __pycache__
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

.PHONY: lint black isort flake8 mypy clean
