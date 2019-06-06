import requests
import json as json
import numpy as np


mlCount = 0
condCount = 0
totalCount = 0

#calculate and print out the prediction based on ML
def get_ML_prediction(data = {"sentence":"I am happy"}):
    # data = data.encode('utf-8')
    url = 'https://5mtavp4jbe.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    decoded_response = json.loads(response) #convert string response to python
    decoded_second = json.loads(decoded_response['body']) #converting body string response to python
    if decoded_second["predicted_label"] == "sorry, I am unable to predict.":
        response = "Sorry, we are unable to make a prediction at this time. Please check your endpoint!"
    elif decoded_second["predicted_label"] == "h":
        response = "you're happy! :) "
    elif decoded_second["predicted_label"] == "s":
        response = "you're sad. :("
    else:
        response = "Based on the null model, we think you are happy! :)"

    print("ML prediction: " + response)

    if response == "Based on the null model, we think you are happy! :)":
        response = "happy"
    elif response == "Sorry, we are unable to make a prediction at this time. Please check your endpoint!":
        response = "undefined"
    return response


#calculate and print out the prediction based on CONDITIONS
def get_conditional_prediction(mood):
    #print(response)
    response = "not sure"
    if "fat" in mood or "sad" in mood:
        response = "sad"
    else:
        response = "happy"

    print("Rules prediction: " + response)
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
        mood = input("Type anything on your mind!")
        type(mood)

        data = {"sentence": mood}
        ml_returned_val = get_ML_prediction(data)
        rules_returned_val = get_conditional_prediction(mood)
        answer = input("Was the prediction \"" + ml_returned_val + "\" correct? (yes/no) ")
        if answer == "yes":
            mlCount+= 1 #ML prediction is correct
            if ml_returned_val == rules_returned_val: #both are correct
                 condCount+=1
        else:
            if rules_returned_val != ml_returned_val:
                condCount+=1
            else:
                print("Looks like we couldn't predict this correctly, oops!")
            

        totalCount+=1
        print("Correct ML responses: " + str(mlCount) + "out of " + str(totalCount) )
        print("Correct rule responses: " + str(condCount) + "out of " + str(totalCount))
        
        play = input("Want to play again? (yes/no) ")
        type(play)
    print("Thanks for playing! Have a great day!")

    






