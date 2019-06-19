import requests
import json as json
import numpy as np



def get_prediction(url, data={"num_countries":48, "years_school":2, "height":5.14}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r, '_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])

    if "dummy response" in prediction_object['Message']:
        print("Please train your model to get better predictions.")
    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']
    else:
        label = "This model is unable to predict at this point."

    print("ML prediction:" + label)
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
                variable = input("You must enter a string.\n" + question)
        break
    return variable


if __name__ == "__main__":

    correct_tries = 0
    tries = 0

    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"


    play = "yes"
    print("Hello! Today we are going to use ML to guess whether you are a child or an adult!")

    url=input("What is your endpoint URL?\n")
    while base_url not in url:
        print("Please make sure your endpoint URL starts with " + base_url)
        url = get_validated_input("What is your endpoint URL?\n", 'string')
    
    while play == "yes":

        visited_countries = get_validated_input("How many countries have you visited?\n", 'integer')
        years_in_school = get_validated_input("How many years did you spend in school?\n", 'integer')
        height = get_validated_input("What is your height?\n", 'float')

    
        data = {"num_countries":visited_countries, "years_school":years_in_school, "height":height}
        get_prediction(url, data)

        tries+=1
        correct = input("Was the model's prediction correct? (yes/no)\n")

        if correct == "yes":
            correct_tries+=1
        
        print("Correct Tries: " + str(correct_tries) + " out of " + str(tries))

        play = input("Want to try again? (yes/no)\n")






