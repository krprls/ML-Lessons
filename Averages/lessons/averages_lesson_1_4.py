import requests
import json as json
import numpy as np



#calculate and print out the prediction
def get_prediction(url, data={"A":48,"B":23,"C":38,"D":54}):
    # data = data.encode('utf-8')
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

    #getting player input 
    correct_tries = tries = 0
    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"
    play = "y"

    print("Hello! Today we are going to try to compute the average of four numbers with Machine Learning!")

    url=input("What is your endpoint URL?\n")
    while base_url not in url:
        print("Please make sure your endpoint URL starts with " + base_url)
        url = get_validated_input("What is your endpoint URL?\n", 'string')
    
    while play.lower() == "y":
        first = get_validated_input("Please enter your first number: ",'float')
        second = get_validated_input("Please enter your second number: ",'float')
        third = get_validated_input("Please enter your third number: ",'float')
        fourth = get_validated_input("Please enter your fourth number: ",'float')

        #pass in the data
        data = {"A": first, "B": second,"C": third, "D": fourth}
 
        get_prediction(url, data)

        tries+=1
        correct_response = input("Was our prediction correct? (y/n)\n")

        if correct_response.lower() == "y":
            correct_tries+=1
        
        print("Correct Tries: " + str(correct_tries) + " out of " + str(tries))
        
        play = input("Want to try again? (y/n)\n")







