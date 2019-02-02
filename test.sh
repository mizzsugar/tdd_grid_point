#!/bin/sh
pytest tests.py
flake8 .
mypy gridpoint.py
