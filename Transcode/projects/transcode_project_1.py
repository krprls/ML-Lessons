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
    values_duration = values['duration']
    values_split = values_duration.split(',')

    arg_list = []

    for a in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'duration'):
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
    fields = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
              'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('Id'), sg.Input(619, key='id')],
              [sg.Text('duration', text_color='red'), sg.Input(42, key='duration')],
              [sg.Text('codec'), sg.Input(2, key='codec')],
              [sg.Text('width'), sg.Input(0, key='width')],
              [sg.Text('height'), sg.Input(1, key='height')],
              [sg.Text('bitrate'), sg.Input(1, key='bitrate')],
              [sg.Text('framerate'), sg.Input(1, key='framerate')],
              [sg.Text('I'), sg.Input(2, key='i')],
              [sg.Text('P'), sg.Input(0, key='p')],
              [sg.Text('B'), sg.Input(1, key='b')],
              [sg.Text('Frames'), sg.Input(1, key='frames')],
              [sg.Text('I_size'), sg.Input(1, key='i_size')],
              [sg.Text('B_size'), sg.Input(101348.88, key='b_size')],
              [sg.Text('Size'), sg.Input(1, key='size')],
              [sg.Text('O_codec'), sg.Input(2, key='o_codec')],
              [sg.Text('O_bitrate'), sg.Input(0, key='o_bitrate')],
              [sg.Text('O_framerate'), sg.Input(1, key='o_framerate')],
              [sg.Text('O_width'), sg.Input(1, key='o_width')],
              [sg.Text('O_height'), sg.Input(1, key='o_height')],
              [sg.Text('Umem'), sg.Input(101348.88, key='umem')],
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
            window.Element('_PRED_').Update('duration: [' + values['duration'] + ']\n' +
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


def get_prediction(url, data='{"id": 0Yxo-eU6AjI,'
                             '"duration": 326.583,'
                             '"codec": vp8,'
                             '"width": 640,'
                             '"height": 480,'
                             '"bitrate": 1055982,'
                             '"framerate": 25.039877,'
                             '"i": 102,'
                             '"p": 8061,'
                             '"b": 0,'
                             '"frames": 8163,'
                             '"i_size": 1868804,'
                             '"b_size": 0,'
                             '"size": 43108248,'
                             '"o_codec": flv,'
                             '"o_bitrate": 5000000,'
                             '"o_framerate": 24,'
                             '"o_width": 480,'
                             '"o_height": 360,'
                             '"umem": 215124}'):
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
