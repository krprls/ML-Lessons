import requests
import json as json
import numpy as np

import argparse
import tkinter as tk
import PySimpleGUI as sg

# Sample format of data expected
# {"longitude":-122.5,"latitude":37.79,"housing_median_age":52,
# "total_rooms":8,"total_bedrooms":1,"population":13,"households":1,
# "median_income":15.0001}):



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
    values_age = values['total_bedrooms']
    values_split = values_age.split(',')

    arg_list = []

    for a in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'total_bedrooms'):
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
    fields = ['longitude', 'latitude', 'housing_median_age',
              'total_rooms', 'total_bedrooms',
              'population', 'households', 'median_income']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('longitude'), sg.Input(-122.5, key='longitude')],
              [sg.Text('latitude'), sg.Input(37.79, key='latitude')],
              [sg.Text('housing_median_age'), sg.Input(52, key='housing_median_age')],
              [sg.Text('total_rooms'), sg.Input(8, key='total_rooms')],
              [sg.Text('total_bedrooms', text_color='red'), sg.Input(1, key='total_bedrooms')],
              [sg.Text('population'), sg.Input(13, key='population')],
              [sg.Text('households'), sg.Input(1, key='households')],
              [sg.Text('median_income'), sg.Input(15.0001, key='median_income')],
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
            window.Element('_PRED_').Update('total_bedrooms: [' + values['total_bedrooms'] + ']\n' + 
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


def get_prediction(url, data='{"longitude":-122.5,"latitude":37.79,'
                             '"housing_median_age":52,"total_rooms":8,'
                             '"total_bedrooms":1,"population":13,'
                             '"households":1, "median_income":15.0001}'):
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
