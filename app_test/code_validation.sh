#!/usr/bin/env bash

# Install dependencies
apt-get update && \
apt-get install make -y && \
apt-get install curl -y \
apt-get install build-essential python-dev -y

python -m install -r ./requirements.txt

# PyTest
sleep 5
pytest --cov=src --cov-report xml:coverage.xml --cov-report term-missin --ignore=setup.py
coverage xml -o coverage.xml
coverage report -m --fail-under=80