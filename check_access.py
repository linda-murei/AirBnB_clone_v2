#!/usr/bin/python3
"""
Check if the Flask application is running.
"""

import subprocess

# Command to check for listening ports using the full path to netstat
command = "/bin/netstat -tln | grep ':5000 '"

# Run the command and capture the output
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)

# Check if the Flask application is running
if result.returncode == 0:
    print("Hello HBNB!")
else:
    print("[Not Running]")

