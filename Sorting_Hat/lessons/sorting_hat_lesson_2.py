import requests
import json as json
import numpy as np


correctRules = 0
correctMl = 0
tries = 0

#calculate and print out the prediction
def get_ML_prediction(data = {"description":"I love to help others!"}):
    # data = data.encode('utf-8')
    url = 'https://6q3r4c6eff.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    decoded_response = json.loads(response) #convert string response to python
    if 'body' not in decoded_response:
            response = "unsure"
    else:
        decoded_second = json.loads(decoded_response['body']) #converting body string response to python
        if "dummy response" in response:
            response = "...based on the null model, we think you are a Hufflepuff!"
        else:
            response = decoded_second['predicted_label']

    print("ML prediction: " + response)

    return response


def get_rules_prediction(sentence="I am ambitious"):
    if "ambitious" in sentence:
        response = "Slytherin"
    elif "friend" in sentence:
        response = "Slytherin"
    elif "creative" in sentence:
        response = "Ravenclaw"
    elif "courage" in sentence:
        response = "Gryffindor"
    else:
        response = "unsure"
    
    print("ML prediction: " + response)
    return response

if __name__ == "__main__":

    play = "yes"
    print("Hello! Today we will sort you into a wizard house!")
    name = input("What is your name? ")
    type(name)
    print("Nice to meet you wizard " + name + "!")
    while play == "yes":
        #getting player input 
        trait = input("Tell me something about yourself! ")
        type(trait)
        #pass in the data
        data = {"description": trait}
        print("Hmm, " + name + ", it seems like...")
        ml_pred = get_ML_prediction(data)
        rules_pred = get_rules_prediction(trait)

        correct_response = input("Is " + "\"" + ml_pred + "\"" + " the correct response? (yes/no) ")
        type(correct_response)

        if "yes" in correct_response:
            correctMl+=1
            if ml_pred == rules_pred:
                correctRules+= 1
        else:
            if ml_pred != rules_pred and rules_pred != "unsure":
                correct_response = input("Is " + "\"" + rules_pred + "\"" + " the correct response? (yes/no) ")
                type(correct_response)
                if "yes" in correct_response:
                    correctRules+=1
                else:
                    print("Aww, looks like neither of our models predicted correctly!")
            else:
                print("Aww, looks like neither of our models predicted correctly!")
        
        tries+=1

        print("Correct ML: " + str(correctMl) + " out of " + str(tries))
        print("Correct Rules: " + str(correctRules) + " out of " + str(tries))
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)
    
    print("Have a great day!")