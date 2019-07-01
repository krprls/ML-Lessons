import requests
import json as json
import numpy as np

def main():
    print("Hello! Today we are going to try to compute the average of four numbers with a Machine Learning model!")

    url = input("What is your endpoint URL?\n")
    url = url.strip()

    num1 = input("Please enter your first number: ")
    num2 = input("Please enter your second number: ")
    num3 = input("Please enter your third number: ")
    num4 = input("Please enter your fourth number: ")

    #pass in the data
    data = {"A": num1, "B": num2,"C": num3, "D": num4}

    get_prediction(url, data)

#calculate and print out the prediction
def get_prediction(url, data={"A":48,"B":23,"C":38,"D":54}):
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
    return label


if __name__ == "__main__":
    main()








