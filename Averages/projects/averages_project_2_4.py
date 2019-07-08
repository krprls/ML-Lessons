import requests
import json as json
import numpy as np

def main():
    tries = 0
    trial_error = 0
    average_error = 0

    print("Hello! Today we are going to try to compute the average of four numbers with a Machine Learning model!")

    url = input("What is your endpoint URL?\n")
    url = url.strip()

    play = "y"
    while play.lower() == "y":
        num1 = input("Please enter your first number: ")
        num2 = input("Please enter your second number: ")
        num3 = input("Please enter your third number: ")
        num4 = input("Please enter your fourth number: ")

        #pass in the data
        data = {"A": num1, "B": num2,"C": num3, "D": num4}
        ml_prediction = get_prediction(url, data) #ML
        ave_via_formula = formula(num1, num2, num3, num4)

        tries += 1
        
        if float(ml_prediction):
            trial_error = abs(ml_prediction - ave_via_formula)
            average_error = (average_error + trial_error) / tries

        print("Error for this trial: ", trial_error)
        print("Average Error: ", average_error)
        print("Total trials: ", tries)
  
        print("Press Ctrl + C to stop at anytime. Moving on to the next round.")

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
    # print("\tMessage: ", prediction_object['Message']) #UNCOMMENT WHEN MESSAGE KEY EXISTS FOR REGRESSION MODELS
    return label

#calculate and print out the prediction based on FORMULA
def formula(num1=50, num2=70, num3=80, num4=90):

    label = (float(num1) + float(num2) + float(num3) + float(num4)) / 4

    print("Average via Formula")
    print("\tLabel: ", label)
    return label

if __name__ == "__main__":
    main()

    






