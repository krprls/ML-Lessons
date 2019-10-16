
import requests
import json as json
import numpy as np

import argparse
import tkinter as tk
import PySimpleGUI as sg

# Sample format of data expected
# {"Pregnancies":6,"Glucose":148,"BloodPressure":72,"SkinThickness":35,
# "Insulin":0,"BMI":33.6,"DiabetesPedigreeFunction":0.627,"Age":50}
# For blank/null values, pass a 'NaN' in the gui so that the prediction can be made.

def inp_replace(inp_val):
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
    values_retweet = values['retweet_count']
    values_split = values_retweet.split(',')

    arg_list = []

    for a in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'retweet_count'):
                body = body + '"' + feature + '"' + ':' + str(values_split[a]) + ','
            else:
                body = body + '"' + feature + '"' + ':' + inp_replace(values[feature]) + ','
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
    fields = ['airline_sentiment_confidence','negativereason','negativereason_confidence','airline','airline_sentiment_gold',
            'retweet_count','text']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('airline_sentiment_confidence'), sg.Input(1.0, key='airline_sentiment_confidence')],
              [sg.Text('negativereason'), sg.Input('', key='negativereason')],
              [sg.Text('negativereason_confidence'), sg.Input('', key='negativereason_confidence')],
              [sg.Text('airline'), sg.Input('Virgin America', key='airline')],
              [sg.Text('airline_sentiment_gold'), sg.Input('', key='airline_sentiment_gold')],
              [sg.Text('text'), sg.Input('@VirginAmerica What @dhepburn said.', key='text')],
              [sg.Text('retweet_count', text_color='red'), sg.Input(0, key='retweet_count')],
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
            window.Element('_PRED_').Update('Retweet Count: [' + values['retweet_count'] + ']\n' +
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


def get_prediction(url, data='{"airline_sentiment_confidence" : 1.0,'
                               '"negativereason" : '','
                               '"negativereason_confidence" : '','
                               '"airline" : Virgin America,'
                               '"airline_sentiment_gold" : '','
                               '"retweet_count" : 0,'
                               '"text" : @VirginAmerica What @dhepburn said.}'):
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
