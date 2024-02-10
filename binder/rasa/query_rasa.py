import ipywidgets as widgets
from IPython.display import display
import json
import requests
import sys
import os
from scripts.preprocessors import preprocessing
from scripts.postprocessings import postprocess

RASA_parse = {}
out = widgets.Output()

# Define a function that will be called when the button is clicked
def handle_submit(sender):
    with out:
        print("User input:", text.value)
    preoutput = preprocessing(text.value)

    payload = {"sender": "Rasa", "text": text.value}
    headers = {'content-type': 'application/json'}
    response = requests.post('http://localhost:5005/model/parse', json=payload, headers=headers)
    rasa_output = response.json()
    intents = rasa_output['intent']['name']

    final = postprocess(rasa_output,preoutput)

    output = final.print_params()

    RASA_parse['intent'] = intents
    RASA_parse['source'] = output['source']
    RASA_parse['destination'] = output['destination']
    RASA_parse['substance'] = output['substance']
    RASA_parse['amount'] = output['amount']
    RASA_parse['units'] = output['units']
    RASA_parse['motion'] = output['motion']
    RASA_parse['action_verb'] = output['action_verb']
    RASA_parse['goal'] = output['goal']

    with out:
        print("final output: ", RASA_parse)
    
# Create a text input widget
text = widgets.Text(description="Enter text:")

# Create a button widget
button = widgets.Button(description="Submit")

# Attach the handle_submit function to the button's click event
button.on_click(handle_submit)

# Display the widgets
display(text)
display(button)
with out:
    print('working')
display(out)