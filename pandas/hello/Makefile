PYTHON_FILES = $(wildcard *.py)
RUN_TARGETS = $(patsubst %.py,run-%,${PYTHON_FILES})

.PHONY: run $(RUN_TARGETS)
run:
	pipenv run python main.py

$(RUN_TARGETS): run-%:
	pipenv run python $*.py

read-csv:
	pipenv run python read-csv.py
