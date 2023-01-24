setup:
	pipenv install --dev

tests:
	pipenv run pytest

lint:
	cd src/ ; \
	pipenv run pylint src/ tests/

fmt:
	pipenv run isort src/ tests/ ; \
	pipenv run black src/ tests/

check_style:
	pipenv run black --check --diff src/ tests/ ; \
	pipenv run isort --check --diff src/ tests/ ; \
	pipenv run pylint --fail-under=7.0 src/ tests/
