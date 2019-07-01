import requests
import json as json
import numpy as np


def main():

    print("Hello! Today we are going to use ML to guess whether you are a child or an adult!")

    url = input("Paste your endpoint URL:\n")
    url = url.strip()
    
    num_countries = input("How many countries has this person visited?\n")
    years_school = input("How many years did this person spend in school?\n")
    height = input("How tall is this person (in feet)?\n")
    
    data = {"num_countries": num_countries, "years_school": years_school, "height": height}
    get_prediction(url, data)

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

if __name__ == "__main__":
    main()






