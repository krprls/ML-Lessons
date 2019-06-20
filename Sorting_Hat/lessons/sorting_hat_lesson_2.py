import requests
import json as json
import numpy as np



def get_prediction(url, data={"description:", "I love to help others!"}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])

    if "dummy response" in prediction_object['Message']:
        print("Please train your model to get better predictions.")
    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']
    else:
        label = "This model is unable to predict at this point."

    print("ML prediction:", label)
    return label


def get_rules_prediction(sentence="I am ambitious"):
    if "ambitious" in sentence:
        response = "Slytherin"
    elif "friend" in sentence:
        response = "Hufflepuff"
    elif "creative" in sentence:
        response = "Ravenclaw"
    elif "courage" in sentence:
        response = "Gryffindor"
    else:
        response = "unsure"
    
    print("ML prediction: " + response)
    return response


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


    correct_rules = 0
    correct_ml = 0
    correct_tries = 0
    tries = 0
    play = "y"
    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"

    print("Today we will use ML to sort you into a Harry Potter wizard house!")
 
    url=input("What is your endpoint URL?\n")
    while base_url not in url:
        print("Please make sure your endpoint URL starts with " + base_url)
        url = get_validated_input("What is your endpoint URL?\n", 'string')
    
    while play.lower() == "y":
        trait = get_validated_input("Tell me something about yourself!\n",'string')

        data = {"description": trait}
        ml_prediction= get_prediction(url, data)
        rules_prediction = get_rules_prediction(trait)

        tries += 1
        correct_response = input("Is " + "\"" + ml_prediction + "\"" + " the correct response? (y/n)\n")
        if correct_response.lower() == "y":
            correct_ml += 1
            if ml_prediction == rules_prediction:
                correct_rules += 1
        else:
            correct_response = input("Is " + "\"" + rules_prediction + "\"" + " the correct response? (y/n)\n")
            if correct_response.lower() == "y":
                correct_rules += 1

      

        print("Correct ML: ", correct_ml, " out of ", tries)
        print("Correct Rules: ", correct_rules, " out of ", tries)
        play = input("Want to try again? (y/n)\n")
    