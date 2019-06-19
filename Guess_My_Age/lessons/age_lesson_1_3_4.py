import requests
import json as json
import numpy as np



def get_prediction(data={"num_countries":48,"years_school":2,"height":5.14},url=''):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction = json.loads(response['body'])

    if "dummy response" in prediction['Message']:
        print("Please train your model to get better predictions. Based on the mock model, the prediction is...")
    
    if "child" in prediction['predicted_label']:
        print("a child!")
    elif "adult" in prediction['predicted_label']:
        print("an adult!")
    else:
        print("The model is unable to predict at this point.")



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
            url = input("Please try re-entering your endpoint URL. Copy the URL directly from your Ai service.\n" + question)
        break
    return variable


if __name__ == "__main__":

    correct_tries = 0
    tries = 0


    play = "yes"
    print("Hello! Today we are going to use ML to guess whether you are a child or an adult!")

    url=input("What is your endpoint URL?\n")
    while not ("https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/" in url):
        url = get_validated_input("What is your endpoint URL?\n", 'string')
    
    while play == "yes":

        visited_countries = get_validated_input("How many countries have you visited?\n",'integer')
        years_in_school = get_validated_input("How many years did you spend in school?\n",'integer')
        height = get_validated_input("What is your height?\n",'float')

    
        data = {"num_countries":visited_countries,"years_school":years_in_school,"height":height}
        print("The model predicts you are...")
        get_prediction(data,url)

        tries+=1
        correct = input("Was our prediction correct? (yes/no)\n")

        if correct == "yes":
            correct_tries+=1
        
        print("Correct Tries: " + str(correct_tries) + " out of " + str(tries))

        play = input("Thank you for playing! Want to try again? (yes/no) ")






