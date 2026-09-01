all: install lint run clean

install:

run:
	python3 a_maze_ing.py config.txt

debug:
	python -m pdb a_maze_ing.py config.txt

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

.PHONY: all  install run debug lint clean

