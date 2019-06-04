import requests
import json as json
import numpy as np

#calculate and print out the prediction
def get_prediction(data = {"sentence":"I am happy"}):
    # data = data.encode('utf-8')
    url = 'https://k4udnfig52.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    print(response)
    if "\"predicted_label\": \"s\"" in response:
        print("you're happy! :) ")
    else:
        print("you're sad. :(")
    return response




if __name__ == "__main__":

    play = "yes"
    while play == "yes":
        #getting player input 
        print("Hello! Today we will guess how you are feeling!")
        mood = input("Type anything on your mind!")
        type(mood)
        

        #pass in the data
        data = {"sentence": "I am happy"}
        print("Hmm, it seems like...")
        get_prediction(data)
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)
    
    print("Have a great day!")