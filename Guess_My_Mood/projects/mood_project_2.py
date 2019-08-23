import requests
import json as json
import numpy as np


def main():
    correct_ml_tries = 0
    correct_rules_tries = 0
    total_tries = 0

    print("Hello! Today we will use machine learning to guess how you are feeling!")

    url = input("What is your endpoint URL?\n")
    url = url.strip()

    while True:

        mood = input("What's on your mind?\n")
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

        print("Press Ctrl + C to stop at anytime. Moving on to the next round.")


#calculate and print out the prediction based on ML 
def get_prediction(url, data={"sentence:", "I am happy"}):
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
def get_conditional_prediction(mood):
    label = "happy"

    if "bad" in mood or "sad" in mood:
        label = "sad"

    print("Rules prediction")
    print("\tLabel: ", label)
    return label

if __name__ == "__main__":
    main()

    