import requests
from threading import Thread
import subprocess
import os
try:
    import rasa
except ImportError:
    print("Rasa package does not exist")
    rasa_command = "rasa run --enable-api"
    process = subprocess.run(rasa_command, shell=True, capture_output=True, text=True)
    import rasa
    print("Rasa installed")
    
def run_bash_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    # print("Output:", process.stdout())
    # if process.stderr:
    #     print("Error:", process.stderr)
    
if __name__ == '__main__':

    # Define your Bash command
    bash_command = "rasa run --enable-api"
    
    # Start Flask app in a separate thread
    bash_thread = Thread(target=run_bash_command, args=(bash_command,))
    bash_thread.start()