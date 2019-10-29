
import requests
import json as json
import numpy as np

import argparse
import tkinter as tk
import PySimpleGUI as sg

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
    values_int_memory = values['int_memory']
    values_split = values_int_memory.split(',')

    arg_list = []

    for a in range(0,len(values_split)):
        args = {'url': values['url']}
        feature_num = 1
        body = '{'
        for feature in fields:
            if(feature == 'int_memory'):
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
    fields = ['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep','mobile_wt','n_cores',
              'pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi']
    layout = [[sg.Text('url'), sg.Input('', key='url')],
              [sg.Text('battery_power'), sg.Input(803 , key='battery_power')],
              [sg.Text('blue'), sg.Input(1 , key='blue')],
              [sg.Text('clock_speed'), sg.Input(2.1, key='clock_speed')],
              [sg.Text('dual_sim'), sg.Input(0, key='dual_sim')],
              [sg.Text('fc'), sg.Input(7, key='fc')],
              [sg.Text('four_g'), sg.Input(0, key='four_g')],
              [sg.Text('int_memory'), sg.Input(17, key='int_memory')],
              [sg.Text('m_dep'), sg.Input(1.0, key='m_dep')],
              [sg.Text('mobile_wt'), sg.Input(198, key='mobile_wt')],
              [sg.Text('n_cores'), sg.Input(4, key='n_cores')],
              [sg.Text('pc'), sg.Input(11, key='pc')],
              [sg.Text('px_height'), sg.Input(344, key='px_height')],
              [sg.Text('px_width'), sg.Input(1440, key='px_width')],
              [sg.Text('ram'), sg.Input(2680, key='ram')],
              [sg.Text('sc_h'), sg.Input(7, key='sc_h')],
              [sg.Text('sc_w'), sg.Input(1, key='sc_w')],
              [sg.Text('talk_time'), sg.Input(4, key='talk_time')],
              [sg.Text('three_g'), sg.Input(1, key='three_g')],
              [sg.Text('touch_screen'), sg.Input(0, key='touch_screen')],
              [sg.Text('wifi', text_color='red'), sg.Input(1, key='wifi')],
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
            window.Element('_PRED_').Update('int_memory: [' + values['int_memory'] + ']\n' +
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


def get_prediction(url, data='{"battery_power" : 803,'
                              '"blue" : 1,'
                              '"clock_speed" : 2.1,'
                              '"dual_sim" : 0,'
                              '"fc" : 7,'
                              '"four_g" : 0,'
                              '"int_memory" : 17,'
                              '"m_dep" : 1.0,'
                              '"mobile_wt" : 198,'
                              '"n_cores" : 4,'
                              '"pc" : 11,'
                              '"px_height" : 344,'
                              '"px_width" : 1440,'
                              '"ram" : 2680,'
                              '"sc_h" : 7,'
                              '"sc_w" : 1,'
                              '"talk_time" : 4,'
                              '"three_g" : 1,'
                              '"touch_screen" : 0,'
                              '"wifi" : 1}'):
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
