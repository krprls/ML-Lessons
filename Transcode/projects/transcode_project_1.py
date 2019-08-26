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
            elif(isinstance(values[feature], str)):
                body = body + '"' + feature + '"' + ':' + '"' + values[feature] + '",'
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
    fields = ['id', 'duration', 'codec', 'width', 'height',
              'bitrate', 'framerate', 'i', 'p', 'b', 'frames',
              'i_size', 'p_size', 'b_size', 'size', 'o_codec',
              'o_bitrate', 'o_framerate', 'o_width',
              'o_height', 'umem']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('id'), sg.Input('0Yxo-eU6AjI', key='id')],
              [sg.Text('duration', text_color='red'), sg.Input(326.583, key='duration')],
              [sg.Text('codec'), sg.Input('vp8', key='codec')],
              [sg.Text('width'), sg.Input(640, key='width')],
              [sg.Text('height'), sg.Input(480, key='height')],
              [sg.Text('bitrate'), sg.Input(1055982, key='bitrate')],
              [sg.Text('framerate'), sg.Input(25.03, key='framerate')],
              [sg.Text('i'), sg.Input(102, key='i')],
              [sg.Text('p'), sg.Input(8061, key='p')],
              [sg.Text('b'), sg.Input(0, key='b')],
              [sg.Text('frames'), sg.Input(8163, key='frames')],
              [sg.Text('i_size'), sg.Input(1, key='i_size')],
              [sg.Text('p_size'), sg.Input(41239444, key='p_size')],
              [sg.Text('b_size'), sg.Input(0, key='b_size')],
              [sg.Text('size'), sg.Input(43108248, key='size')],
              [sg.Text('o_codec'), sg.Input("fly", key='o_codec')],
              [sg.Text('o_bitrate'), sg.Input(5000000, key='o_bitrate')],
              [sg.Text('o_framerate'), sg.Input(24, key='o_framerate')],
              [sg.Text('o_width'), sg.Input(480, key='o_width')],
              [sg.Text('o_height'), sg.Input(360, key='o_height')],
              [sg.Text('umem'), sg.Input(215124, key='umem')],
              [sg.Text('Prediction: ', text_color='blue', size=(40, 2), key='_PRED_')],
              [sg.RButton('Predict'), sg.Exit()]]
    window = sg.Window('Enter url and feature values', layout)
    while True:
        event, values = window.Read()
        predictions = str(get_multiple_predictions(values, fields))
        predictions.replace('"', '')
        if event == 'Predict':
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
                             '"p_size": 41239444,'
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
