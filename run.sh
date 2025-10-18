#!/bin/bash

if [ ! -d "venv" ]; then
    echo "venv folder doesn't exist!"
    exit 1
else
    ./venv/bin/python3 main.py
fi
