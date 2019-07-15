
import requests
import json as json
import numpy as np

import argparse
import tkinter as tk
import PySimpleGUI as sg

# Sample format of data expected
# {"Pregnancies":6,"Glucose":148,"BloodPressure":72,"SkinThickness":35,
# "Insulin":0,"BMI":33.6,"DiabetesPedigreeFunction":0.627,"Age":50}

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
    values_age = values['Age']
    values_split = values_age.split(',')

    arg_list = []

    for a in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'Age'):
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
    fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
              'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('Pregnancies'), sg.Input(6, key='Pregnancies')],
              [sg.Text('Glucose'), sg.Input(148, key='Glucose')],
              [sg.Text('BloodPressure'), sg.Input(72, key='BloodPressure')],
              [sg.Text('SkinThickness'), sg.Input(35, key='SkinThickness')],
              [sg.Text('Insulin'), sg.Input(0, key='Insulin')],
              [sg.Text('BMI'), sg.Input(33.6, key='BMI')],
              [sg.Text('DiabetesPedigreeFunction'), sg.Input(0.627, key='DiabetesPedigreeFunction')],
              [sg.Text('Age', text_color='red'), sg.Input(50, key='Age')],
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
            window.Element('_PRED_').Update('Age: [' + values['Age'] + ']\n' + 
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


def get_prediction(url, data='{"Pregnancies":6,'
                             '"Glucose":148,'
                             '"BloodPressure":72,'
                             '"SkinThickness":35,'
                             '"Insulin":0,'
                             '"BMI":33.6,'
                             '"DiabetesPedigreeFunction":0.627,'
                             '"Age":50}'):
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
        args_list = ui_mode()
