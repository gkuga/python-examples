PYTHON_FILES = $(wildcard *.py)
RUN_TARGETS = $(patsubst %.py,run-%,${PYTHON_FILES})

.PHONY: run $(RUN_TARGETS)
run:
	python3 src/main.py

.PHONY: venv
venv:
	python3 -m venv .venv

.PHONY: install-e
install-e:
	.venv/bin/pip install -e .

.PHONY: install
install:
	.venv/bin/pip install .

.PHONY: test
test:
	.venv/bin/python -m unittest discover -s tests

$(RUN_TARGETS): run-%:
	python3 $*.py
