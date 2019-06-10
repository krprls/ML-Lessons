import requests
import json as json
import numpy as np


mlCount = 0
formulaCount = 0
totalCount = 0

#calculate and print out the prediction based on ML
def get_ML_prediction(data={"A":48,"B":23,"C":38,"D":54}):
    # data = data.encode('utf-8')
    url = 'https://jzsbkydi4g.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    decoded_response = json.loads(response) #convert string response to python

    if "dummy response" in response:
        response = "based on the null model, we think the average is 472!"
    elif "error" in response:
        response = "..hmm..looks like we couldn't predict, please only enter numbers."
    else:
        decoded_second = json.loads(decoded_response['body']) #converting body string response to python
        response = decoded_second["predicted_label"]

    print("ML prediction: " + str(response))  

    if response == "based on the null model, we think the average is 472!":
        response = 472

    return response


#calculate and print out the prediction based on FORMULA
def formula(num1=50,num2=70,num3=80,num4=90):

    response=""
    try: 
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        num4 = float(num4)
        response = (num1 + num2 + num3 + num4)/4
    except ValueError:
        response = "not sure"
    

    print("Formula: " + str(response)) 

    return response


if __name__ == "__main__":

    #getting player input 
    print("Hello! Today we are going to guess how you feel!")
    name = input("What is your name? ")
    type(name)
    print("Nice to meet you " + name + "!")

    play = "yes"
    while play == "yes":
        #get user input
        first = input("Please enter your first number: ")
        type(first)
        second = input("Please enter your second number: ")
        type(second)
        third = input("Please enter your third number: ")
        type(third)
        fourth = input("Please enter your fourth number: ")
        type(fourth)


        #pass in the data
        data = {"A": first, "B": second,"C": third, "D": fourth}
        ml_returned_val = get_ML_prediction(data) #ML
        rules_returned_val = formula(first,second,third,fourth)

        if ml_returned_val != "..hmm..looks like we couldn't predict, please only enter numbers.":
            if abs(ml_returned_val - rules_returned_val) < 0.01:
                mlCount+=1
            formulaCount+=1 #formula is always correct
            totalCount+=1


        print("Correct ML responses: " + str(mlCount) + " out of " + str(totalCount) )
        print("Correct rule responses: " + str(formulaCount) + " out of " + str(totalCount))
        
        play = input("Want to play again? (yes/no) ")
        type(play)
    print("Thanks for playing! Have a great day!")

    






