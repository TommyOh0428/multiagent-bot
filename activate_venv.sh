#!/usr/bin/env bash

echo "Activating virtual environment"

if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found. Please create it first."
    exit 1
fi

echo "Running on OS: $OSTYPE"

# if macos, use this command
if [[ "$OSTYPE" == "darwin"* ]]; then
    source ./.venv/bin/activate
fi
# if windows, use the following command
if [[ "$OSTYPE" == "msys" ]]; then
    .\venv\Scripts\activate
fi
# if linux, use the following command
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    source ./.venv/bin/activate
fi