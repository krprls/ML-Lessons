
import requests
import json as json
import numpy as np

import argparse
import tkinter as tk
import PySimpleGUI as sg

# Sample format of data expected
# {"Pregnancies":6,"Glucose":148,"BloodPressure":72,"SkinThickness":35,
# "Insulin":0,"BMI":33.6,"DiabetesPedigreeFunction":0.627,"Age":50}

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
    values_age = values['job_age_days']
    values_split = values_age.split(',')

    arg_list = []

    for a in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'job_age_days'):
                body = body + '"' + feature + '"' + ':' + str(values_split[a]) + ','
            else:
                body = body + '"' + feature + '"' + ':' + wrap_string_in_quotes(values[feature]) + ','
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
    fields = ['title_proximity_tfidf', 'description_proximity_tfidf', 'main_query_tfidf', 'query_jl_score',
              'query_title_score', 'city_match', 'job_age_days', 'search_date_pacific','class_id']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('title_proximity_tfidf'), sg.Input(0.0 , key='title_proximity_tfidf')],
              [sg.Text('description_proximity_tfidf'), sg.Input(0.19837657 , key='description_proximity_tfidf')],
              [sg.Text('main_query_tfidf'), sg.Input(0.0, key='main_query_tfidf')],
              [sg.Text('query_jl_score'), sg.Input(0.02254546, key='query_jl_score')],
              [sg.Text('query_title_score'), sg.Input(0.014705882, key='query_title_score')],
              [sg.Text('city_match'), sg.Input(1.0, key='city_match')],
              [sg.Text('job_age_days'), sg.Input(16.0, key='job_age_days')],
              [sg.Text('search_date_pacific', text_color='red'), sg.Input('2018-01-24', key='search_date_pacific')],
              [sg.Text('class_id', text_color='red'), sg.Input(-1305520379511432611, key='class_id')],
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
            window.Element('_PRED_').Update('job_age_days: [' + values['job_age_days'] + ']\n' +
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


def get_prediction(url, data='{"title_proximity_tfidf" : 0.0,'
                              '"description_proximity_tfidf" : 0.19837657,'
                              '"main_query_tfidf" : 0.0,'
                              '"query_jl_score" : 0.02254546  ,'
                              '"query_title_score" : 0.014705882 ,'
                              '"city_match" : 1.0,'
                              '"job_age_days" : 16.0,'
                              '"search_date_pacific" : 2018-01-24,'
                              '"class_id" : -1305520379511432611}'):
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
