import requests
import json as json
import numpy as np

#calculate and print out the prediction
def get_prediction(data = {"data":"I am happy"}):
    # data = data.encode('utf-8')
    url = 'https://6pnvtgf9md.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    #print(response)
    if np.float(response) == 0:
        print("you're happy! :) ")
    else:
        print("you're sad. :(")
    return response




if __name__ == "__main__":

    #getting player input 
    print("Hello! Today we will guess how you are feeling!")
    mood = input("Type anything on your mind!")
    type(mood)

    #pass in the data
    data = {"data": mood}
    print("Hmm, it seems like you are...")
    get_prediction(data)