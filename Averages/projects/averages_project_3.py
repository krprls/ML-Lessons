import requests
import json as json
import numpy as np



#calculate and print out the prediction based on ML
def get_prediction(dataset_size, url, data={"A":48,"B":23,"C":38,"D":54}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])

    if 'Message' in prediction_object and "dummy response" in prediction_object['Message']:
        print("Please train your model to get better predictions.")
    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']
    else:
        label = "This model is unable to predict at this point."

    if dataset_size == "small":
        print("ML prediction (smaller dataset): ", label)
    else:
        print("ML prediction (bigger dataset): ", label)

    return label

#calculate and print out the prediction based on FORMULA
def formula(num1=50,num2=70,num3=80,num4=90):

    average = ""
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    num4 = float(num4)
    average = (num1 + num2 + num3 + num4) / 4

    print("Average via Formula: ", average)

    return average

def get_validated_input(question,input_type):

    variable = input(question)

    while True:
        if input_type == 'float':
            try:
                user_input = float(variable)
            except ValueError:
                variable = input("You must enter a float (e.g.: 1.3).\n" + question)
        elif input_type == 'integer':
            try:
                user_input = int(variable)
            except ValueError:
                variable = input("You must enter an integer (e.g.: 1).\n" + question)
        elif input_type == 'string':
             try:
                user_input = str(variable)
             except ValueError:
                variable = input("You must enter a string.\n" + question)
        break
    return variable

if __name__ == "__main__":

    tries = 0
    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"
    average_error_new = average_error_old = 0


    print("Hello! Today we are going to try to compute the average of four numbers with a Machine Learning model!")

    old_url = input("What is your endpoint URL from your SMALLER (i.e., with smaller dataset) Ai service?\n")
    while base_url not in old_url:
        print("Please make sure your endpoint URL starts with " + base_url)
        old_url = get_validated_input("What is your endpoint URL from your SMALLER (i.e., with smaller dataset) Ai service?\n", 'string')
    old_url = old_url.strip()


    new_url = input("What is your endpoint URL from your BIGGER (i.e., with larger dataset) Ai service?\n")
    while base_url not in new_url:
        print("Please make sure your endpoint URL starts with " + base_url)
        new_url = get_validated_input("What is your endpoint URL from your BIGGER (i.e., with larger dataset) Ai service?\n", 'string')
    new_url = new_url.strip()

    play = "y"
    while play.lower() == "y":
        trial_error_new = trial_error_old = 0
        
        #get user input
        num1 = get_validated_input("Please enter your first number: ", 'float')
        num2 = get_validated_input("Please enter your second number: ", 'float')
        num3 = get_validated_input("Please enter your third number: ", 'float')
        num4 = get_validated_input("Please enter your fourth number: ", 'float')

        #pass in the data
        data = {"A": num1, "B": num2,"C": num3, "D": num4}
        old_ml_prediction = get_prediction("small", old_url, data) #from smaller dataset
        new_ml_prediction = get_prediction("big", new_url, data) #from bigger dataset

        ave_via_formula = formula(num1, num2, num3, num4)

 

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
  
        
        play = input("Want to play again? (y/n)\n")
 

    






