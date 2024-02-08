import rasa
import requests
from threading import Thread
import subprocess
import os

# dir = os.getcwd()
# newdir = './binder/rasa'
#
# if dir != newdir:
#     try:
#         os.chdir(newdir)
#         print("Changed directory to:", newdir)
#     except FileNotFoundError:
#         print("Directory not found:", newdir)
# else:
#     print("Already in the desired directory:", newdir)

def run_bash_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("Output:", process.stdout())
    if process.stderr:
        print("Error:", process.stderr)
    
if __name__ == '__main__':

    # bash_install = "pip install rasa"
    # process = subprocess.run(bash_install, shell=True, capture_output=True, text=True)
    # print("Output:", process.stdout())

    # Define your Bash command
    bash_command = "rasa run --enable-api"
    
    # Start Flask app in a separate thread
    bash_thread = Thread(target=run_bash_command, args=(bash_command,))
    bash_thread.start()
    
# Define your Bash command
# bash_command = "rasa run --enable-api"

# Run the Bash command
# result = subprocess.run(bash_command, shell=True, capture_output=True, text=True)

# Print the output
# print("Output:", result.stdout)

# Print the error message if any
# if result.stderr:
    # print("Error:", result.stderr)