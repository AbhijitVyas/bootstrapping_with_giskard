import requests
from threading import Thread
import subprocess
import os
import time
flag = True

try:
    import rasa
except ImportError:
    print("RASA package does not exist")
    print('Installing RASA')
    rasa_command = "pip install -q rasa"
    # process = subprocess.run(rasa_command, shell=True, capture_output=True, text=True)
    process = subprocess.Popen(rasa_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
    import rasa
    print("RASA installed and Imported")
    
def run_bash_command(command):
    # process = subprocess.run(command, shell=True, capture_output=True, text=True)
    # print("Rasa command")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print('Starting RASA Server',end='')
    for line in iter(process.stdout.readline, ''):
        # print(line, end='')
        if 'up and running' in line:
          break
    # print("Rasa Server is UP AND RUNNING")
    global flag
    flag = False
    
if __name__ == '__main__':

    # Define your Bash command
    bash_command = "rasa run --enable-api"
    
    # Start Flask app in a separate thread
    bash_thread = Thread(target=run_bash_command, args=(bash_command,))
    bash_thread.start()
    
    while True:
        time.sleep(3)
        if not flag:
            print('SERVER READY')
            break
        else:
            print(".",end='')