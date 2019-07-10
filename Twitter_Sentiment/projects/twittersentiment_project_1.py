import requests
import json as json
import numpy as np

def main():
    print("Hello! Today we are going to try to classify an expression's sentiment with a Machine Learning model!")

    url = input("What is your endpoint URL?\n")
    url = url.strip()

    expression = input("What's on your mind?\n")
    data ={"Expression": expression}

    get_prediction(url, data)
    print("Sentiment is on a scale from 0-4, with 0=negative, 2=neutral, and 4=positive.")

#calculate and print out the prediction
def get_prediction(url, data={"Expression": "@DaRealSunisaKim Thanks for the Twitter add, Sunisa!" 
                              + "I got to meet you once at a HIN show here in the DC area and you were a sweetheart. "}):
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
    print("\tMessage: ", prediction_object['Message']) #UNCOMMENT WHEN MESSAGE KEY EXISTS FOR REGRESSION MODELS
    return label


if __name__ == "__main__":
    main()
