.PHONY: install run

VENV := .venv
PYTHON := $(VENV)/bin/python

install:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run:
	@test -x $(PYTHON) || (echo "Run make install first." && exit 1)
	$(PYTHON) run_notebook.py
