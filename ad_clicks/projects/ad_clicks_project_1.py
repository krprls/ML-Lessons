

import requests
import json as json
import numpy as np

import argparse
import tkinter as tk
import PySimpleGUI as sg


def wrap_string_in_quotes(inp_val):
    if isinstance(inp_val, str):
        inp_val.replace('"', '')
        return '"' + inp_val + '"'
    else:
        return inp_val

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
                body = body + '"' + feature + '"' + ':' + wrap_string_in_quotes(values[feature]) + ','
            feature_num = feature_num+1
        body = body[0:-1] + '}'
        args['body'] = body
        arg_list.append(args)
    predictions = []
    my_index = 0
    for queries in arg_list:
        my_index += 1
        print("What gets sent: ", queries['body'])
        prediction = json.loads(get_prediction(queries['url'], queries['body']))
        print(prediction)
        pred_value = json.loads(prediction['body'])['predicted_label']
        predictions.append(pred_value)
    return predictions


def ui_mode():
    """
    This function generates a UI where the user can enter
    feature values and see responses
    """
    # Create a dialog box with the features
    fields = ['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage','Ad Topic Line','City',
              'Male', 'Country', 'Timestamp']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('Daily Time Spent on Site'), sg.Input(68.95, key='Daily Time Spent on Site')],
              [sg.Text('Age', text_color='red'), sg.Input(35, key='Age')],
              [sg.Text('Area Income'), sg.Input(61833.9, key='Area Income')],
              [sg.Text('Daily Internet Usage'), sg.Input(256.09, key='Daily Internet Usage')],
              [sg.Text('Ad Topic Line'), sg.Input('Cloned 5thgeneration orchestration', key='Ad Topic Line')],
              [sg.Text('City'), sg.Input('Wrightburgh', key='City')],
              [sg.Text('Male'), sg.Input(0, key='Male')],
              [sg.Text('Country'), sg.Input('Tunisia', key='Country')],
              [sg.Text('Timestamp'), sg.Input('2016-03-27 00:53:11', key='Timestamp')],
              [sg.Text('Prediction: ', text_color='blue', size=(40, 2), key='_PRED_')],
              [sg.RButton('Predict'), sg.Exit()]]

    window = sg.Window('Enter url and feature values', layout)
    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break

        predictions = str(get_multiple_predictions(values, fields))
        predictions.replace('"', '')
        if event == 'Predict':
            print('entered predict event')
            # change the "output" element to be the value of "input" element
            window.Element('_PRED_').Update('Age: [' + values['Age'] + ']\n' +
                                            'Prediction: ' + predictions)


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


def get_prediction(url, data='{"Daily Time Spent on Site" : 68.95,'
                             ' "Area Income" : 61833.9,'
                             ' "Daily Internet Usage" : 256.09,'
                             ' "Ad Topic Line" : "Cloned 5thgeneration orchestration",'
                             ' "City" : "Wrightburgh",'
                             ' "Male" : 0,'
                             ' "Country" : "Tunisia",'
                             ' "Timestamp" : "2016-03-27 00:53:11",'
                             ' "Age" : 35}'):
    r = requests.post(url, data=data)
    response = getattr(r, '_content').decode("utf-8")
    print(response)
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
