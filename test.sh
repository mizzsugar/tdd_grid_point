#!/bin/sh
pytest -v tests.py
flake8 gridpoint.py tests.py
mypy gridpoint.py
