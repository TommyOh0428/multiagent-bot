#!/usr/bin/env bash

echo "Activating virtual environment"

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