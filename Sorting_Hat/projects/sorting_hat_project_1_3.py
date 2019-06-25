import requests
import json as json
import numpy as np



#calculate and print out the prediction based on ML 
def get_prediction(url, data={"description:", "I love to help others!"}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])

    if 'Message' in prediction_object and "dummy response" in prediction_object['Message']:
        print("Please train your model to get better predictions.")
    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']

    print("ML Prediction: ", label)
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

    correct_tries = 0
    tries = 0
    play = "y"
    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"

    print("Today we will use ML to sort you into a Harry Potter wizard house!")
 
    url = input("What is your endpoint URL?\n")
    while base_url not in url:
        print("Please make sure your endpoint URL starts with " + base_url)
        url = get_validated_input("What is your endpoint URL?\n", 'string')
    url = url.strip()

    while play.lower() == "y":
        trait = get_validated_input("Tell me something about yourself!\n",'string')

        data = {"description": trait}
        ml_prediction = get_prediction(url, data)

        if ml_prediction != "Unable to predict":
            tries += 1
            correct = input("Was the model's prediction correct? (y/n)\n")
            if correct.lower() == "y":
                correct_tries += 1 

        print("Correct Tries: ", correct_tries,  " out of ", tries)

        play = input("Want to try again? (y/n)\n")

    