#!/bin/bash

# Activate virtual environment
source /Users/venyasharma/recyclo_backend/venv/bin/activate

# Change to project directory
cd /Users/venyasharma/recyclo_backend

# Run your retrain script
python retrain_from_misclass.py

# Deactivate virtual environment
deactivate

