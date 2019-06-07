import requests
import json as json
import numpy as np


mlCount = 0
condCount = 0
totalCount = 0

#calculate and print out the prediction based on ML
def get_ML_prediction(data = {"sentence":"I am happy"}):
    # data = data.encode('utf-8')
    url = 'https://6ur5sl3hh6.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    decoded_response = json.loads(response) #convert string response to python
    decoded_second = json.loads(decoded_response['body']) #converting body string response to python
    if "dummy response" in response:
        response = "based on the null model, we think the average is 472!"
    elif "error" in response:
        response = "error"
    else:
        response = decoded_second["predicted_label"]

    if response == "based on the null model, we think the average is 472!":
        response = 472

    print("ML prediction: " + str(response)) 
    return response


#calculate and print out the prediction based on CONDITIONS
def get_conditional_prediction(arr=np.array(13,300,901,21)):
    response = "not sure"
    first_set= np.array(410 , 306 , 525 , 431)
    second_set= np.array(850 , 69 , 112 , 324)
   
    #data passed in more similar to first set
    if np.linalg.norm(arr-first_set) < np.linalg.norm(arr-second_set):
        response= 418.0
    else:
        response= 338.75

    print("Rules prediction: " + str(response))
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
        first = input("Please enter your first number(between 0-1000): ")
        type(first)
        second = input("Please enter your second number(between 0-1000): ")
        type(second)
        third = input("Please enter your third number(between 0-1000): ")
        type(third)
        fourth = input("Please enter your fourth number(between 0-1000): ")
        type(fourth)


        #pass in the data
        data = {"A": first, "B": second,"C": third, "D": fourth}
        ml_returned_val = get_ML_prediction(data) #ML
        rules_returned_val = get_conditional_prediction(np.array(np.float(first),np.float(second),np.float(third),np.float(fourth))) #rules/conditional


        #Tally the scores of ml and rules count 
        answer = input("Was the prediction \"" + ml_returned_val + "\" correct? (yes/no) ")
        if answer == "yes":
            mlCount+= 1 #ML prediction is correct
            if ml_returned_val == rules_returned_val: #both are correct
                 condCount+=1
        else:
            if rules_returned_val != ml_returned_val and ml_returned_val != "error": #only rules is correct
                condCount+=1
            else:
                print("Looks like we couldn't predict this correctly, oops!") #neither is correct
            

        totalCount+=1
        print("Correct ML responses: " + str(mlCount) + "out of " + str(totalCount) )
        print("Correct rule responses: " + str(condCount) + "out of " + str(totalCount))
        
        play = input("Want to play again? (yes/no) ")
        type(play)
    print("Thanks for playing! Have a great day!")

    






