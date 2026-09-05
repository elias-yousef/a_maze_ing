all: install lint run

install:
	python3 -m pip install -e .
	python3 -m pip install build

build:
	python3 -m build

run:
	python3 a_maze_ing.py config.txt

debug:
	python3 -m pdb a_maze_ing.py config.txt

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf build
	rm -rf *.egg-info
	rm -rf src/__pycache__

.PHONY: all install build run debug lint clean
