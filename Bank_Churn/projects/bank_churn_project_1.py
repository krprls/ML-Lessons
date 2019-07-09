
import requests
import json as json
import numpy as np

def main():

    print("Hello! Today we will use ML to see if a person will leave a bank!")

    url = input("What is your endpoint URL?\n")
    url = url.strip()

    #get user input 
    credit_score = input("What is this person's credit score?\n")
    age = input("How old is this person?\n")
    tenure = input("How many years has this person been with the bank?\n")
    balance = input("What is this person's bank account balance?\n")
    products = input("How many products does this person have?\n")
    is_credit_card_holder = input("Does this person have a credit card? (enter 1 for yes or 0 for no)\n")
    is_active_member = input("Is this person an active member of the bank? (enter 1 for yes or 0 for no)\n")
    salary = input("How much does this person earn annually?\n")

    #pass in the data
    data = {"CreditScore": credit_score, "Age": age, "Tenure": tenure, "Balance": balance, "NumOfProducts": products,
                "HasCrCard": is_credit_card_holder, "IsActiveMember": is_active_member, "EstimatedSalary": salary}

    print("(1.0 means exited, 0.0 means has not exited)")
    get_prediction(url, data)

    

def get_prediction(url, data={"CreditScore": 600, "Age": 35, "Tenure": 5, "Balance": 47575.50, "NumOfProducts": 5,
                                    "HasCrCard": 1, "IsActiveMember": 1, "EstimatedSalary": 300000.50}):
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