import requests
import json as json
import numpy as np




url = ''
#calculate and print out the prediction based on ML 
def get_prediction(url,data={"num_countries":48,"years_school":2,"height":5.14}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction = json.loads(response['body'])

    if "dummy response" in prediction['Message']:
        print("Please train your model to get better predictions. Based on the mock model, the prediction is...")
    
    if prediction['predicted_label'] == "child" or prediction['predicted_label'] == "adult":
        response = prediction['predicted_label']
    else:
        response = "This model is unable to predict at this point."

    print("ML prediction:" + response)
    return response


#calculate and print out the prediction based on CONDITIONS
def get_conditional_prediction(countries, years, height):
    response = "This model is unable to predict at this point."
    if np.float(countries) > 10 and np.float(years) > 10 and np.float(height) > 3:
        response = "adult"
    else:
        response = "child"

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

    correct_ml_tries = 0
    correct_rules_tries = 0
    total_tries = 0


    play = "yes"
    print("Hello! Today we are going to use ML to guess whether you are a child or an adult!")

    url=input("What is your endpoint URL?\n")
    while not ("https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/" in url):
        print("Please make sure your endpoint URL starts with https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/")
        url = get_validated_input("What is your endpoint URL?\n", 'string')
    
    while play == "yes":

        visited_countries = get_validated_input("How many countries have you visited?\n",'integer')
        years_in_school = get_validated_input("How many years did you spend in school?\n",'integer')
        height = get_validated_input("What is your height?\n",'float')

    
        data = {"num_countries":visited_countries,"years_school":years_in_school,"height":height}

        ml_response = get_prediction(url,data)
        rules_response = get_conditional_prediction(visited_countries,years_in_school,height)

        total_tries += 1
        user_validation = input("Was the prediction \"" + ml_response + "\" correct? (yes/no)\n")

        if user_validation == "yes":
            correct_ml_tries += 1
            if ml_response == rules_response:
                correct_rules_tries += 1
        else:
            if rules_response != "This model is unable to predict at this point.":
                user_validation = input("Was the prediction \"" + rules_response + "\" correct? (yes/no)\n")
                if user_validation == "yes":
                    correct_rules_tries += 1
        
        print("Correct ML Tries: " + str(correct_ml_tries) + " out of " + str(total_tries))
        print("Correct Rules Tries: " + str(correct_rules_tries) + " out of " + str(total_tries))

        play = input("Want to try again? (yes/no)\n")

    