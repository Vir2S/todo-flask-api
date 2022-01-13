.PHONY: all \
		setup \
		black \
		flake8

venv/bin/activate: ## alias for virtual environment
	python -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

black: venv/bin/activate ## Run black
	. venv/bin/activate; black -l 79 .

flake8: venv/bin/activate ## Run flake
	. venv/bin/activate; flake8 .
