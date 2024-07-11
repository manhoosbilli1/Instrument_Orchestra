#!/bin/bash

# Define the remote server details
REMOTE_USER="your_remote_username"
REMOTE_HOST="your_remote_host"
REMOTE_PYTHON_SCRIPT_PATH="/path/to/hmp4040_control.py"
OUTPUT_FILE="hmp4040_output.txt"

# Execute the Python script on the remote server and save the output locally
ssh $REMOTE_USER@$REMOTE_HOST "python3 $REMOTE_PYTHON_SCRIPT_PATH" > $OUTPUT_FILE

# Check if the command ran successfully
if [ $? -eq 0 ]; then
    echo "Output successfully written to $OUTPUT_FILE"
else
    echo "An error occurred while running the Python script on the remote server"
    exit 1
fi
