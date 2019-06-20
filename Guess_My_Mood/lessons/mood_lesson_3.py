import requests
import json as json
import numpy as np

#calculate and print out the prediction based on ML
def get_prediction(url, data={"sentence": "I am happy."}):
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

    print("ML prediction:", label)
    return label


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
    correct_old_tries = correct_new_tries = 0

    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"

    play = "y"
    print("Hello! Today we will use machine learning to guess how you are feeling!")

    old_url = input("What is your endpoint URL from your OLDER (i.e., with smaller dataset) Ai service?\n")
    while base_url not in old_url:
        print("Please make sure your endpoint URL starts with " + base_url)
        old_url = get_validated_input("What is your endpoint URL from your OLDER (i.e., with smaller dataset) Ai service?\n", 'string')


    new_url = input("What is your endpoint URL from your NEWER (i.e., with larger dataset) Ai service?\n")
    while base_url not in new_url:
        print("Please make sure your endpoint URL starts with " + base_url)
        new_url = get_validated_input("What is your endpoint URL from your NEWER (i.e., with larger dataset) Ai service?\n", 'string')


    while play.lower() == "y":
        trial_error_new = trial_error_old = 0
        
        #get user input
        mood = get_validated_input("What's on your mind?\n", 'string')

        #pass in the data
        data = {"sentence": mood}
        old_ml_prediction = get_prediction(old_url, data) #from smaller dataset
        new_ml_prediction = get_prediction(new_url, data) #from bigger dataset

        tries += 1
        print("Keep in mind s = sad and h = happy")
        user_validation = input("Was the prediction based on the newer model, \"" + new_ml_prediction + "\", correct? (y/n)\n")

        if user_validation.lower() == "y":
            correct_new_tries += 1
            if old_ml_prediction == new_ml_prediction:
                correct_old_tries += 1
        elif old_ml_prediction != new_ml_prediction and old_ml_prediction != "This model is unable to predict at this point.":
            correct_old_tries += 1
        

        print("Correct tries, OLDER dataset: ", correct_old_tries)
        print("Correct tries, NEWER dataset: ", correct_new_tries)
        print("Total trials: ", tries)
        
        play = input("Want to play again? (y/n)\n")
 

    






