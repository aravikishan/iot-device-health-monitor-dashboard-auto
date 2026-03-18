#!/bin/bash
set -e
echo "Starting IoT Device Health Monitor Dashboard..."
uvicorn app:app --host 0.0.0.0 --port 9029 --workers 1
