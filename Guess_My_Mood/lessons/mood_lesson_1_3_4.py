import requests
import json as json
import numpy as np

url = ''

#calculate and print out the prediction
def get_prediction(data = {"sentence":"I am happy"}):
    # data = data.encode('utf-8')
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    decoded_response = json.loads(response) #convert string response to python
    if 'body' not in decoded_response:
            response = "unsure"
    else:
        decoded_second = json.loads(decoded_response['body']) #converting body string response to python
        if decoded_second["predicted_label"] == "h":
            response = "you're happy! :) "
        elif decoded_second["predicted_label"] == "s":
            response = "you're sad. :("
        else:
            response = "Based on the null model, we think you are happy! :)"
    print("ML prediction: " + response)

    return response




if __name__ == "__main__":

    play = "yes"
    print("Hello! Today we will guess how you are feeling!")
    name = input("What is your name? ")
    type(name)
    print("Nice to meet you " + name + "!")

    url = input("Before we get started, what is your endpoint URL?")
    type(url)
    print("Thank you!")
    
    while play == "yes":
        #getting player input 
        mood = input("Type anything on your mind! ")
        type(mood)
        #pass in the data
        data = {"sentence": mood}
        print("Hmm, " + name + ", it seems like...")
        get_prediction(data)
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)
    
    print("Have a great day!")