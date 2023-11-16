# python-challenges WIP

## List of Content

1. [Overview](#overview)
1. [Installation and Setup Instructions](#installation-and-setup-instructions)
1. [Usage Instruction](#usage-instruction)
1. [File Structure](#file-structure)
1. [License](#license)

## Overview

This repo includes Python challenges collected from several publicly available resources on the internet. These challenges are solved through a test-driven development process using the pytest library. All solution scripts are written in compliance with PEP8 standards, and you can run all checks using Make commands.


## Installation and Setup Instructions

All installation and setup requirements are conveniently encapsulated in a Makefile. Follow these simple commands:

- Create a virtual environment:
```bash
    make create-venv
```
- Install Flake8:
```bash
    make install-flake
```
- Install Pytest:
```bash
    make install-pytest
```
## Usage Instruction
All commands to run tests and check for complaiance with PEP8 are conveniently encapsulated in a Makefile. Follow these simple commands:

Run all pytest tests and check for compliance with PEP8 standards:
```bash
    make run-checks
```
Run all pytest tests:
```bash
    make test-all
```
Run test for a specific file:
```bash
    make unit-test "file_name"
```
Check for compliance with PEP8 standards:
```bash
    make run-flake
```

## File Structure
```bash

```

## License
