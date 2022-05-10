SHELL := /bin/bash

init:
	@pip install -r requirements-dev.txt -r requirements.txt

lint:
	flake8 app/ tests/ main.py
	black --line-length 79 --check app/ tests/ main.py

unit:
	pytest --disable-pytest-warnings tests/unit/

test: unit

run: lint test