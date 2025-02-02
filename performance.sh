#!/bin/bash

echo "Performing tasks on $(date +%Y-%m-%d)"
echo

echo "Running pylint..."
echo "-----------------"

# Run pylint on the python files
pylint $(git ls-files '*.py') | tee -a performance.log

echo

echo "Running pytest..."
echo "-----------------"

# Run pytest on the test files
pytest | tee -a performance.log

echo
echo "All the logs are saved in performace.log"
