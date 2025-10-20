#!/bin/bash
# Simple script to run the Speech Command Recognizer using the correct virtual environment

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PY="$SCRIPT_DIR/../.venv/bin/python"

exec "$VENV_PY" "$SCRIPT_DIR/Speech_Command_Recognizer.py"
