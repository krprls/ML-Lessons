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
    values_age = values['tenure']
    values_split = values_age.split(',')

    arg_list = []

    for a in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'tenure'):
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
    fields = ['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService',
              'OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract',
              'PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']
    layout = [[sg.Text('url'), sg.Input('https://7b7qhlx1yh.execute-api.us-east-1.amazonaws.com/Predict/9f5c170d-f2ca-432e-b658-dc12f03327aa', key='url')],
              [sg.Text('gender'), sg.Input('Male', key='gender')],
              [sg.Text('SeniorCitizen'), sg.Input(0, key='SeniorCitizen')],
              [sg.Text('Partner', text_color='red'), sg.Input('No', key='Partner')],
              [sg.Text('Dependents'), sg.Input('No', key='Dependents')],
              [sg.Text('tenure'), sg.Input(34, key='tenure')],
              [sg.Text('PhoneService'), sg.Input('Yes', key='PhoneService')],
              [sg.Text('MultipleLines'), sg.Input('No', key='MultipleLines')],
              [sg.Text('InternetService'), sg.Input('DSL', key='InternetService')],
              [sg.Text('OnlineSecurity'), sg.Input('Yes', key='OnlineSecurity')],
              [sg.Text('OnlineBackup'), sg.Input('No', key='OnlineBackup')],
              [sg.Text('DeviceProtection'), sg.Input('Yes', key='DeviceProtection')],
              [sg.Text('TechSupport'), sg.Input('No', key='TechSupport')],
              [sg.Text('StreamingTV'), sg.Input('No', key='StreamingTV')],
              [sg.Text('StreamingMovies'), sg.Input('No', key='StreamingMovies')],
              [sg.Text('Contract'), sg.Input('One year', key='Contract')],
              [sg.Text('PaperlessBilling'), sg.Input('No', key='PaperlessBilling')],
              [sg.Text('PaymentMethod'), sg.Input('Mailed check', key='PaymentMethod')],
              [sg.Text('MonthlyCharges'), sg.Input('56.95', key='MonthlyCharges')],
              [sg.Text('TotalCharges'), sg.Input('1889.5', key='TotalCharges')],
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
            window.Element('_PRED_').Update('tenure: [' + values['tenure'] + ']\n' +
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


def get_prediction(url, data='{"gender" : Male, '
                             ' "SeniorCitizen" : 0, '
                             ' "Partner" : No, '
                             ' "Dependents" : No, '
                             ' "tenure" : 34, '
                             ' "PhoneService" : Yes, '
                             ' "MultipleLines" : No, '
                             ' "InternetService" : DSL, '
                             ' "OnlineSecurity" : Yes, '
                             ' "OnlineBackup" : No, '
                             ' "DeviceProtection" : Yes, '
                             ' "TechSupport" : No, '
                             ' "StreamingTV" : No, '
                             ' "StreamingMovies" : No, '
                             ' "Contract" : One year, '
                             ' "PaperlessBilling" : No, '
                             ' "PaymentMethod" : Mailed check, '
                             ' "MonthlyCharges" : 56.95, '
                             ' "TotalCharges" : 1889.5} '):
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
