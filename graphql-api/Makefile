SHELL := /bin/bash

init:
	@pip install -r requirements-dev.txt -r requirements.txt

lint:
	flake8 app/ main.py
	black --line-length 79 --check app/ main.py

run: lint