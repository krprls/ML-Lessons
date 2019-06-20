import requests
import json as json
import numpy as np


mlCount = 0
formulaCount = 0
totalCount = 0

url = ''
#calculate and print out the prediction
def get_prediction(url, data={"A":48,"B":23,"C":38,"D":54}):
    # data = data.encode('utf-8')
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])

    if "dummy response" in prediction_object['Message']:
        print("Please train your model to get better predictions.")
    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']
    else:
        label = "This model is unable to predict at this point."

    print("ML prediction:" + label)
    return label


#calculate and print out the prediction based on FORMULA
def formula(num1=50,num2=70,num3=80,num4=90):

    response=""
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    num4 = float(num4)
    response = (num1 + num2 + num3 + num4)/4

    print("Formula: " + str(response)) 

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


    print("Hello! Today we are going to try to compute the average of four numbers with Machine Learning!")


    url = input("Before we get started, what is your endpoint URL?")
    type(url)
    print("Thank you!")

    play = "yes"
    while play == "yes":
        first = get_validated_input("Please enter your first number: ",'float')
        second = get_validated_input("Please enter your second number: ",'float')
        third = get_validated_input("Please enter your third number: ",'float')
        fourth = get_validated_input("Please enter your fourth number: ",'float')




        data = {"A": first, "B": second,"C": third, "D": fourth}
        ml_returned_val = get_prediction(data) #ML
        rules_returned_val = formula(first,second,third,fourth)

        trialError = 'NaN'
        averageError = 'NaN'
        if ml_returned_val != "This model is unable to predict at this point.":
            totalCount+=1
            trialError = abs(ml_returned_val - rules_returned_val)
            averageError = (averageError + trialError)/totalCount

        print("Error for this trial: " + str(trialError))
        print("Average Error: " + str(averageError))
        print("Total trials: " + str(totalCount))
  
        
        play = input("Want to play again? (y/n)\n")

    print("Thanks for playing! Have a great day!")

    






