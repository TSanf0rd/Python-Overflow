#!/bin/bash

echo "Building Docker image for PythonOverflow..."
docker build -t pythonoverflow .

echo "Running container on port 5000..."
docker run -d -p 5000:5000 pythonoverflow

echo "PythonOverflow is now running at http://localhost:5000"
