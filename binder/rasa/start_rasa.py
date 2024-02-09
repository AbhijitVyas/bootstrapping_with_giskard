import requests
from threading import Thread
import subprocess
import os
try:
    import rasa
except ImportError:
    print("Rasa package does not exist")
    rasa_command = "pip install rasa"
    process = subprocess.run(rasa_command, shell=True, capture_output=True, text=True)
    import rasa
    print("Rasa installed and Imported")
    
def run_bash_command(command):
    # process = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("Rasa command")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
    # print("Output:", process.stdout())
    # if process.stderr:
    #     print("Error:", process.stderr)
    
if __name__ == '__main__':

    # Define your Bash command
    bash_command = "rasa run --enable-api"
    
    # Start Flask app in a separate thread
    bash_thread = Thread(target=run_bash_command, args=(bash_command,))
    bash_thread.start()