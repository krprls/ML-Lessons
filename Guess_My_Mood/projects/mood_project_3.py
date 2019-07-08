import requests
import json as json
import numpy as np


def main():
    tries = 0
    correct_old_tries = correct_new_tries = 0

    print("Hello! Today we will use machine learning to guess how you are feeling!")

    old_url = input("What is your endpoint URL from your OLDER (i.e., with smaller dataset) Ai service?\n")
    old_url = old_url.strip()

    new_url = input("What is your endpoint URL from your NEWER (i.e., with larger dataset) Ai service?\n")
    new_url = new_url.strip()

    while True:
        #get user input
        mood = input("What's on your mind?\n")

        #pass in the data
        data = {"sentence": mood}
        print("ML prediction (smaller dataset)")
        old_ml_prediction = get_prediction(old_url, data) #from smaller dataset
        print("ML prediction (bigger dataset)")
        new_ml_prediction = get_prediction(new_url, data) #from bigger dataset
        
        if old_ml_prediction != "Unable to predict" and new_ml_prediction != "Unable to predict":
            tries += 1
            user_validation = input("Was the prediction based on the newer model, \"" + new_ml_prediction + "\", correct? (y/n)\n")
            if user_validation.lower() == "y":
                correct_new_tries += 1
                if old_ml_prediction == new_ml_prediction:
                    correct_old_tries += 1
            elif old_ml_prediction != new_ml_prediction:
                correct_old_tries += 1
        

        print("Correct tries, OLDER dataset: ", correct_old_tries)
        print("Correct tries, NEWER dataset: ", correct_new_tries)
        print("Total trials: ", tries)
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

    print("\tLabel: ", label)
    print("\tModel: ", prediction_object['Model'])
    print("\tMessage: ", prediction_object['Message'])
    return label

if __name__ == "__main__":
    main()
    