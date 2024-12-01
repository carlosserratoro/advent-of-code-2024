# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

.PHONY: test_all run_script run_black

install:
	@pip install -e src

black:
	@black src/
	@black tests/

test:
ifdef day
	@python -m pytest tests/day_$(day)
else
	@python -m pytest tests
endif

run:
	@python src/aoc/day_$(day)/part_1.py
	@python src/aoc/day_$(day)/part_2.py
