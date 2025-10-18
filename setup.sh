#!/bin/bash

echo ""
echo "========================================"
echo "   	 Installing Steam App"
echo "========================================"
echo ""

if [ ! -d "venv" ]; then
    echo "[1/2] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error creating venv!"
        exit 1
    fi
    echo "Venv created"
else
    echo "Venv already exists"
fi

echo ""
echo "[2/2] Installing dependencies..."
./venv/bin/pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error installing packages!"
    exit 1
fi

echo ""
echo "========================================"
echo "		Installation complete!"
echo "========================================"
echo ""
echo "Run the app using ./run.sh"
echo ""