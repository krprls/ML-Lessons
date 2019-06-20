import requests
import json as json
import numpy as np



#calculate and print out the prediction based on ML
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

    total_count = 0
    base_url = "https://cqzuqwmdp1.execute-api.us-east-1.amazonaws.com/Predict/"


    print("Hello! Today we are going to try to compute the average of four numbers with Machine Learning!")

    old_url=input("What is your endpoint URL from your SMALLER/OLDER Ai service?\n")
    while base_url not in old_url:
        print("Please make sure your endpoint URL starts with " + base_url)
        old_url = get_validated_input("What is your endpoint URL from your SMALLER/OLDER Ai service?\n", 'string')


    new_url=input("What is your endpoint URL from your BIGGER/NEWER Ai service?\n")
    while base_url not in new_url:
        print("Please make sure your endpoint URL starts with " + base_url)
        new_url = get_validated_input("What is your endpoint URL from your BIGGER/NEWER Ai service?\n", 'string')


    play = "y"
    while play.lower() == "y":
        #get user input
        first = get_validated_input("Please enter your first number: ",'float')
        second = get_validated_input("Please enter your second number: ",'float')
        third = get_validated_input("Please enter your third number: ",'float')
        fourth = get_validated_input("Please enter your fourth number: ",'float')


        #pass in the data
        data = {"A": first, "B": second,"C": third, "D": fourth}
        old_ml_returned_val = get_prediction(data, old_url) #from smaller dataset
        new_ml_returned_val = get_prediction(data, new_url) #from bigger dataset

        formula_value = formula(first,second,third,fourth)


        trial_error_new = trial_error_old = 'NaN'
        average_error_new = average_error_old = 'NaN'
        if old_ml_returned_val != "..hmm..looks like we couldn't predict, please only enter numbers.":
            total_count+=1
            trial_error_old = abs(old_ml_returned_val - formula_value)
            average_error_old= (average_error_old + trial_error_old)/total_count

            trial_error_new = abs(new_ml_returned_val - formula_value)
            average_error_new  = (average_error_new + trial_error_new)/total_count

        print("Error for this trial, SMALLER dataset: " + str(trial_error_old))
        print("Error for this trial, BIGGER dataset: " + str(trial_error_new))
        print("Average Error, SMALLER dataset: " + str(average_error_old))
        print("Average Error, BIGGER dataset: " + str(average_error_new))
        print("Total trials: " + str(total_count))
  
        
        play = input("Want to play again? (y/n)\n")


    






