import requests
import json as json
import numpy as np


def main():
    correct_ml_tries = 0
    correct_rules_tries = 0
    total_tries = 0

    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"

    play = "y"
    print("Hello! Today we will use machine learning to guess how you are feeling!")

    url = input("What is your endpoint URL?\n")
    while base_url not in url:
        print("Please make sure your endpoint URL starts with " + base_url)
        url = get_validated_input("What is your endpoint URL?\n", 'string')
    url = url.strip()
    
    while play.lower() == "y":

        mood = get_validated_input("What's on your mind?\n", 'string')

        data = {"sentence": mood}

        ml_prediction = get_prediction(url, data)
        rules_prediction = get_conditional_prediction(mood)


        total_tries += 1
        user_validation = input("Was the rules prediction \"" + rules_prediction + "\" correct? (y/n)\n")

        if user_validation.lower() == "y":
            correct_rules_tries += 1
            if ml_prediction == rules_prediction:
                correct_ml_tries += 1
        elif ml_prediction != rules_prediction and ml_prediction != "Unable to predict":
                correct_ml_tries += 1
            
        print("Correct ML Tries: ", correct_ml_tries, " out of ", total_tries)
        print("Correct Rules Tries: ", correct_rules_tries, " out of ", total_tries)

        play = input("Want to try again? (y/n)\n")

            
#calculate and print out the prediction based on ML 
def get_prediction(url, data={"sentence:", "I love to help others!"}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])

    if 'Message' in prediction_object and "dummy response" in prediction_object['Message']:
        print("Please train your model to get better predictions.")
    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']

    print("ML prediction: ", label)
    return label

#calculate and print out the prediction based on CONDITIONS
def get_conditional_prediction(mood):
    prediction = "happy"

    if "bad" in mood or "sad" in mood:
        prediction = "sad"


    print("Rules prediction: ", prediction)
    return prediction

def get_validated_input(question, input_type):

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
    main()

    