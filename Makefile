help:
	@echo List of available command:
	@echo setup_project: Install packages with poetry
	@echo test: Run tests
	@echo run: Run webscrapping script

setup_project:
	poetry install

test:
	poetry run pytest

run:
	@python todays_matches/main.py 