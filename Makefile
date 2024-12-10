# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

.PHONY: install lint test test_no_solution run

install:
	@pip install -e src

lint:
	@isort src/ tests/
	@black src/ tests/
	@flake8 src/ tests/
	@pylint src/ tests/

test:
ifdef day
	@python -m pytest tests/day_$(day)
else
	@python -m pytest tests
endif

test_no_solution:
ifdef day
	@python -m pytest -m "not solution" tests/day_$(day)
else
	@python -m pytest -m "not solution" tests
endif

run:
	@python src/aoc/day_$(day)/part_1.py
	@python src/aoc/day_$(day)/part_2.py
