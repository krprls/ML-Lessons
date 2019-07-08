import requests
import json as json
import numpy as np


def main():
    correct_rules = 0
    correct_ml = 0
    tries = 0

    play = "y"
    print("Today we will use ML to sort you into a Harry Potter wizard house!")
 
    url = input("What is your endpoint URL?\n")
    url = url.strip()  

    while play.lower() == "y":
        trait = input("Tell me something about yourself!\n")

        data = {"description": trait}
        ml_prediction = get_prediction(url, data)
        rules_prediction = get_rules_prediction(trait)

        if ml_prediction != "Unable to predict":
            tries += 1
            correct_response = input("Is the model's prediction " + "\"" + ml_prediction + "\"" + " the correct response? (y/n)\n")
            if correct_response.lower() == "y":
                correct_ml += 1
                if ml_prediction == rules_prediction:
                    correct_rules += 1
            else:
                correct_response = input("Is the rule's prediction " + "\"" + rules_prediction + "\"" + " the correct response? (y/n)\n")
                if correct_response.lower() == "y":
                    correct_rules += 1
        
        print("Correct ML: ", correct_ml, " out of ", tries)
        print("Correct Rules: ", correct_rules, " out of ", tries)
        print("Press Ctrl + C to stop at anytime. Moving on to the next round.")

#calculate and print out the prediction based on ML 
def get_prediction(url, data={"description:", "I love to help others!"}):
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

def get_rules_prediction(sentence="I am ambitious"):
    label = "Unable to predict"

    if "ambitious" in sentence:
        label = "Slytherin"
    elif "friend" in sentence:
        label = "Hufflepuff"
    elif "creative" in sentence:
        label = "Ravenclaw"
    elif "courage" in sentence:
        label = "Gryffindor"

    print("Rules prediction")
    print("\tLabel: ", label)
    return label

if __name__ == "__main__":
    main()

        
    