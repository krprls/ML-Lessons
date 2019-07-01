import requests
import json as json
import numpy as np

def main():

    print("Today we will use ML to sort you into a Harry Potter wizard house!")
 
    url = input("What is your endpoint URL?\n")
    url = url.strip()

    trait = input("Tell me something about yourself!\n")

    data = {"description": trait}
    get_prediction(url, data)

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

if __name__ == "__main__":
    main()




    