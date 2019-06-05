import requests
import json as json
import numpy as np

#calculate and print out the prediction
def get_prediction(data = {"sentence":"I am happy"}):
    # data = data.encode('utf-8')
    url = 'https://5mtavp4jbe.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    decoded_response = json.loads(response) #convert string response to python
    decoded_second = json.loads(decoded_response['body']) #converting body string response to python
    if decoded_second["predicted_label"] == "sorry, I am unable to predict.":
        print("Sorry, we are unable to make a prediction at this time. Please check your endpoint!")
    elif decoded_second["predicted_label"] == "h":
        print("you're happy! :) ")
    elif decoded_second["predicted_label"] == "s":
        print("you're sad. :(")
    else:
        print("Based on the null model, we think you are happy! :)")
    return response




if __name__ == "__main__":

    play = "yes"
    while play == "yes":
        #getting player input 
        print("Hello! Today we will guess how you are feeling!")
        mood = input("Type anything on your mind!")
        type(mood)
        
        #pass in the data
        data = {"sentence": mood}
        print(data)
        print("Hmm, it seems like...")
        get_prediction(data)
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)
    
    print("Have a great day!")