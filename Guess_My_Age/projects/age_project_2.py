import requests
import json as json
import numpy as np

def main():

    correct_ml_tries = 0
    correct_rules_tries = 0
    total_tries = 0

    print("Hello! Today we are going to use ML to guess whether you are a child or an adult!")

    url = input("What is your endpoint URL?\n")
    
    play = "y"
    while play == "y":
        visited_countries = input("How many countries have you visited?\n")
        years_in_school = input("How many years did you spend in school?\n")
        height = input("What is your height?\n")


        data = {"num_countries":visited_countries, "years_school":years_in_school, "height":height}

        ml_prediction = get_prediction(url, data)
        rules_prediction = get_conditional_prediction(int(visited_countries), int(years_in_school), float(height))

        total_tries += 1
        user_validation = input("Was the rules prediction \"" + rules_prediction + "\" correct? (y/n)\n")

        if user_validation.lower() == "y":
            correct_rules_tries += 1
            if ml_prediction == rules_prediction:
                correct_ml_tries += 1
        elif ml_prediction != rules_prediction and ml_prediction != "Unable to predict.":
            correct_ml_tries += 1
        
        print("Correct ML Tries: ", correct_ml_tries, " out of ", total_tries)
        print("Correct Rules Tries: ", correct_rules_tries, " out of ", total_tries)

        print("Press Ctrl + C to stop at anytime. Moving on to the next round.")
            

#calculate and print out the prediction based on ML 
def get_prediction(url, data={"num_countries":48, "years_school":2, "height":5.14}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])
    label = ""    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']

    print("ML prediction") 
    print("\tLabel: ", label)
    print("\tModel: ", prediction_object['Model'])
    print("\tMessage: ", prediction_object['Message'])
    return label


#calculate and print out the prediction based on CONDITIONS
def get_conditional_prediction(countries, years, height):
    label = "child"

    if countries > 10 and years > 10 and height > 3:
        label = "adult"

    print("Rules prediction")
    print("\tLabel: ", label)
    return label

if __name__ == "__main__":
    main()

    