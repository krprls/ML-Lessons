import requests
import json as json
import numpy as np


#calculate and print out the prediction
def get_prediction(url, flag, data={"A":48,"B":23,"C":38,"D":54}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])
    label = ""    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']

    if flag == 'smaller':
        print("ML prediction (smaller dataset)")
    else:
        print("ML prediction (bigger dataset)")

    print("\tLabel: ", label)
    print("\tModel: ", prediction_object['Model'])
    #print("\tMessage: ", prediction_object['Message']) #UNCOMMENT WHEN MESSAGE KEY PART OF BODY FOR REGRESSION PROJECTS
    return label

#calculate and print out the prediction based on FORMULA
def formula(num1=50, num2=70, num3=80, num4=90):

    label = (float(num1) + float(num2) + float(num3) + float(num4)) / 4

    print("Average via Formula")
    print("\tLabel: ", label)
    return label

if __name__ == "__main__":

    tries = 0
    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"
    average_error_new = average_error_old = 0

    print("Hello! Today we are going to try to compute the average of four numbers with a Machine Learning model!")

    old_url = input("What is your endpoint URL from your OLDER (i.e., with smaller dataset) Ai service?\n")
    old_url = old_url.strip()

    new_url = input("What is your endpoint URL from your NEWER (i.e., with larger dataset) Ai service?\n")
    new_url = new_url.strip()

    while True:
        trial_error_new = trial_error_old = 0
        
        #get user input
        num1 = input("Please enter your first number: ")
        num2 = input("Please enter your second number: ")
        num3 = input("Please enter your third number: ")
        num4 = input("Please enter your fourth number: ")

        #pass in the data
        data = {"A": num1, "B": num2,"C": num3, "D": num4}

        old_ml_prediction = get_prediction(old_url, 'smaller', data) #from smaller dataset
        new_ml_prediction = get_prediction(new_url, 'bigger', data) #from bigger dataset
        ave_via_formula = formula(num1, num2, num3, num4) #from formula

        tries += 1
        if float(old_ml_prediction):
            trial_error_old = abs(old_ml_prediction - ave_via_formula)
            average_error_old = (average_error_old + trial_error_old) / tries

        if float(new_ml_prediction):
            trial_error_new = abs(new_ml_prediction - ave_via_formula)
            average_error_new = (average_error_new + trial_error_new) / tries

        print("Error for this trial, SMALLER dataset: ", trial_error_old)
        print("Error for this trial, BIGGER dataset: ", trial_error_new)
        print("Average Error, SMALLER dataset: ", average_error_old)
        print("Average Error, BIGGER dataset: ", average_error_new)
        print("Total trials: ", tries)
        print("Press Ctrl + C to stop at anytime. Moving on to the next round.")
 

    






