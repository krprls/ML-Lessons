import requests
import json as json
import numpy as np

import argparse
import tkinter as tk
import PySimpleGUI as sg

# Sample format of data expected
# {"age":37,"sex":1,"cp":3,
# "trestbps":130,"chol":250,
# "fbs":0,"restecg":0,"thalach":187,
# "exang":0, "oldpeak":3.5, "slop":3,
# "ca":0, "thal":3}


def get_multiple_predictions(values, fields):
    """
    This function calculates the predictions on
    multiple samples
    Args:
    values (dict): Dictionary containing url and feature values
    fields (list): List of strings containing feature names
    Returns:
    predictions (list): Contains the list of predictions
    """
    values_age = values['age']
    values_split = values_age.split(',')

    arg_list = []

    for a in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'age'):
                body = body + '"' + feature + '"' + ':' + str(values_split[a]) + ','
            else:
                body = body + '"' + feature + '"' + ':' + str(values[feature]) + ','
            feature_num = feature_num+1
        body = body[0:-1] + '}'
        args['body'] = body
        arg_list.append(args)
    predictions = []
    for queries in arg_list:
        prediction = json.loads(get_prediction(queries['url'],
                                               queries['body']))
        pred_value = json.loads(prediction['body'])['predicted_label']
        predictions.append(pred_value)
    return predictions


def ui_mode():
    """
    This function generates a UI where the user can enter
    feature values and see responses
    """
    # Create a dialog box with the features
    fields = ['age', 'sex', 'cp', 'trestbps', 'chol',
              'fbs', 'restecg', 'thalach', 'exang',
              'oldpeak', 'slop', 'ca', 'thal']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('age', text_color='red'), sg.Input(37, key='age')],
              [sg.Text('sex'), sg.Input(1, key='sex')],
              [sg.Text('cp'), sg.Input(3, key='cp')],
              [sg.Text('trestbps'), sg.Input(130, key='trestbps')],
              [sg.Text('chol'), sg.Input(250, key='chol')],
              [sg.Text('fbs'), sg.Input(0, key='fbs')],
              [sg.Text('restecg'), sg.Input(0, key='restecg')],
              [sg.Text('thalach'), sg.Input(187, key='thalach')],
              [sg.Text('exang'), sg.Input(0, key='exang')],
              [sg.Text('oldpeak'), sg.Input(3.5, key='oldpeak')],
              [sg.Text('slop'), sg.Input(3, key='slop')],
              [sg.Text('ca'), sg.Input(0, key='ca')],
              [sg.Text('thal'), sg.Input(3, key='thal')],
              [sg.Text('Prediction: ', text_color='blue', size=(40, 2), key='_PRED_')],
              [sg.RButton('Predict'), sg.Exit()]]
    window = sg.Window('Enter url and feature values', layout)
    while True:
        event, values = window.Read()
        predictions = str(get_multiple_predictions(values, fields))
        predictions.replace('"', '')
        if event == 'Predict':
            print('entered predict event')
            # change the "output" element to be the value of "input" element
            window.Element('_PRED_').Update('age: [' + values['age'] + ']\n' + 
                                            'Prediction: ' + predictions)
        if event is None or event == 'Exit':
            break

    window.Close()


def parseArguments():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Positional mandatory arguments
    parser.add_argument("--body", help="text in the format provided by snippet in Navigator", type=str)
    parser.add_argument("--url", help="Your endpoint URL", type=str)

    # Parse arguments
    try:
        args = parser.parse_args()
    except:
        return None

    return args


def get_prediction(url, data='{"age":37,"sex":1,"cp":3,'
                             '"trestbps":130,"chol":250,'
                             '"fbs":0,"restecg":0,"thalach":187,'
                             '"exang":0, "oldpeak":3.5, "slop":3,'
                             '"ca":0, "thal":3}'):
    r = requests.post(url, data=data)
    response = getattr(r, '_content').decode("utf-8")
    return response

if __name__ == '__main__':
    # Parse the arguments
    # Return None when no arguments are provided
    args = parseArguments()
    print('args: ', args)
    # Print the arguments provided, when present
    if args.url and args.body:
        for a in args.__dict__:
            print(str(a) + ": " + str(args.__dict__[a]))
        print(get_prediction(args.url, args.body))
    else:
        # When no arguments are provided, pop up a
        # dialog box where the user can enter 
        # arguments
        ui_mode()
