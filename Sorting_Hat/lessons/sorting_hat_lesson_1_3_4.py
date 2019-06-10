import requests
import json as json
import numpy as np

#calculate and print out the prediction
def get_prediction(data = {"description":"I love to help others!"}):
    # data = data.encode('utf-8')
    url = 'https://p1bi1qedoj.execute-api.us-east-1.amazonaws.com/Predict'
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

    print(response)

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
        print("Hmm, " + name + ", it seems like you are a...")
        get_prediction(data)
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)
    
    print("Have a great day!")