# Makefile to run these challenges

# Project configuration
PROJECT_NAME = python-challenges
PYTHON := python
VENV_NAME := venv
PIP:=pip
WD=$(shell pwd)
PYTHONPATH=${WD}

# Targets

# create virtual environemnt
create-venv:
	@echo "Creating virtual environment..."
	@$(PYTHON) -m venv $(VENV_NAME)
	@echo "Virtual environment created."


# execute_in_env target is a generic macro to run commands within the virtual environment
# Note: It's not a typical target that will be executed directly, but rather a utility for other targets.
.PHONY: execute_in_env

# Define the execute_in_env macro to activate the virtual environment and run a specified command
ACTIVATE_ENV := source venv/bin/activate

define execute_in_env
    $(ACTIVATE_ENV) && $1
endef

# packages setup
## Install flake8
install-flake:
	$(call execute_in_env, $(PIP) install flake8)

## Install pytest
install-pytest:
	$(call execute_in_env, $(PIP) install pytest)



# Common Commands
## Run a single test
unit-test:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v ${test_run})

## Run all the unit tests
test-all:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v)

## Run the flake8 code check
run-flake:
	$(call execute_in_env, flake8 \
	./src/alphabet_position/*.py \
	./src/bubble_sort/*.py \
	./test/*.py )

## Run all checks
run-checks: test-all run-flake