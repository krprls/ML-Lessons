import requests
import json as json
import numpy as np
import argparse
import tkinter as tk
import PySimpleGUI as sg


# Sample format of data expected
# {"CreditScore":619,"Age":42,"Tenure":2,"Balance":0,"NumOfProducts":1,"HasCrCard":1,"IsActiveMember":1,"EstimatedSalary":101348.88}

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
    age_list = values['Age']
    values_split = age_list.split(',')

    arg_list = []

    for index in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'Age'):
                body = body + '"' + feature + '"' + ':' + str(values_split[index]) + ','
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
    fields = ['Music', 'Movies', 'Horror', 'Thriller', 'Comedy',
              'Romantic', 'Sci-fi', 'War', 'Fantasy/Fairy tales', 
              'Animated', 'Documentary', 'Western', 'Action', 'History', 
              'Mathematics', 'Physics', 'Internet', 'PC', 'Reading', 
              'Cars', 'Shopping', 'Science and technology', 'Adrenaline sports', 
              'Flying', 'Age', 'college/bachelor degree', 'currently a primary school pupil', 
              'doctorate degree', 'masters degree', 'primary school', 'secondary school', 
              'few hours a day', 'less than an hour a day', 'most of the day', 'no time at all']

    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('Music'), sg.Input(5, key='Music')],
              [sg.Text('Movies'), sg.Input(5, key='Movies')],
              [sg.Text('Horror'), sg.Input(4, key='Horror')],
              [sg.Text('Thriller'), sg.Input(2, key='Thriller')],
              [sg.Text('Comedy'), sg.Input(5, key='Comedy')],
              [sg.Text('Romantic'), sg.Input(4, key='Romantic')],
              [sg.Text('Sci-fi'), sg.Input(4, key='Sci-fi')],
              [sg.Text('War'), sg.Input(1, key='War')],
              [sg.Text('Fantasy/Fairy tales'), sg.Input(5, key='Fantasy/Fairy tales')],
              [sg.Text('Animated'), sg.Input(5, key='Animated')],
              [sg.Text('Documentary'), sg.Input(3, key='Documentary')],
              [sg.Text('Western'), sg.Input(1, key='Western')],
              [sg.Text('Action'), sg.Input(2, key='Action')],
              [sg.Text('History'), sg.Input(1, key='History')],
              [sg.Text('Mathematics'), sg.Input(3, key='Mathematics')],
              [sg.Text('Physics'), sg.Input(3, key='Physics')],
              [sg.Text('Internet'), sg.Input(5, key='Internet')],
              [sg.Text('PC'), sg.Input(3, key='PC')],
              [sg.Text('Reading'), sg.Input(3, key='Reading')],
              [sg.Text('Cars'), sg.Input(1, key='Cars')],
              [sg.Text('Shopping'), sg.Input(4, key='Shopping')],
              [sg.Text('Science and technology'), sg.Input(4, key='Science and technology')],
              [sg.Text('Adrenaline sports'), sg.Input(4, key='Adrenaline sports')],
              [sg.Text('Flying'), sg.Input(1, key='Flying')],
              [sg.Text('Age', text_color='red'), sg.Input(20, key='Age')],
              [sg.Text('college/bachelor degree'), sg.Input(1, key='college/bachelor degree')],
              [sg.Text('currently a primary school pupil'), sg.Input(0, key='currently a primary school pupil')],
              [sg.Text('doctorate degree'), sg.Input(0, key='doctorate degree')],
              [sg.Text('masters degree'), sg.Input(0, key='masters degree')],
              [sg.Text('primary school'), sg.Input(0, key='primary school')],
              [sg.Text('secondary school'), sg.Input(0, key='secondary school')],
              [sg.Text('few hours a day'), sg.Input(1, key='few hours a day')],
              [sg.Text('less than an hour a day'), sg.Input(0, key='less than an hour a day')],
              [sg.Text('most of the day'), sg.Input(0, key='most of the day')],
              [sg.Text('no time at all'), sg.Input(0, key='no time at all')],
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


def get_prediction(url, data='{"Music": 5,'
                             '"Movies": 5,'
                             '"Horror": 4,'
                             '"Thriller": 2,'
                             '"Comedy": 5,'
                             '"Romantic": 4,'
                             '"Sci-fi": 4,'
                             '"War": 1,'
                             '"Fantasy/Fairy tales": 5,'
                             '"Animated": 5,'
                             '"Documentary": 3,'
                             '"Western": 1,'
                             '"Action": 2,'
                             '"History": 1,'
                             '"Mathematics": 3,'
                             '"Physics": 3,'
                             '"Internet": 5,'
                             '"PC": 3,'
                             '"Reading": 3,'
                             '"Cars": 1,'
                             '"Shopping": 4,'
                             '"Science and technology": 4,'
                             '"Adrenaline sports": 4,'
                             '"Flying": 1,'
                             '"Age": 20,'
                             '"college/bachelor degree": 1,'
                             '"currently a primary school pupil": 0,'
                             '"doctorate degree": 0,'
                             '"masters degree": 0,'
                             '"primary school": 0,'
                             '"secondary school": 0,'
                             '"few hours a day": 1,'
                             '"less than an hour a day": 0,'
                             '"most of the day": 0,'
                             '"no time at all": 0}'):
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
