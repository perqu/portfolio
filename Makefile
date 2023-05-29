# Zmienne
PYTHON = python
PIP = pip
PROJECT_NAME = portfolio

# Cele
.PHONY: install run test lint format

reqs:
	$(PYTHON) reqs.py

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) manage.py runserver

test:
	$(PYTHON) manage.py test

lint:
	pylint *.py --exit-zero

format:
	black ../$(PROJECT_NAME)

all: lint format reqs install test
