#!/usr/bin/python3
"""
Check if the Flask application is running.
"""

import os

# Check if the Python process associated with Flask is running
def is_flask_running():
    process_name = "web_flask.0-hello_route.py"
    try:
        # Use pgrep to find the process ID (PID) based on the process name
        pid = int(os.popen(f"pgrep -f {process_name}").read())
        return pid is not None
    except ValueError:
        return False

# Check if the Flask application is running
if is_flask_running():
    print("Hello HBNB!")
else:
    print("[Not Running]")

