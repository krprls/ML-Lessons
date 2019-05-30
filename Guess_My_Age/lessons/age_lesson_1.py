import requests
import json as json
import numpy as np

#calculate and print out the prediction
def get_prediction(data = {"data":"10,5,5.41"}):
    # data = data.encode('utf-8')
    url = 'https://m9nh9k61vk.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    #print(response)
    if "0.0" in response:
        print("a child!")
    else:
        print("an adult!")
    return response


if __name__ == "__main__":

    #getting player input 
    play = "yes"
    while play == "yes":
        print("Hello! Today we are going to guess whether you are a child or an adult! ")
        name = input("What is your name? ")
        type(name)
        print("Nice to meet you " + name + "!")
        visitedCountries = input("How many countries have you visited? ")
        type(visitedCountries)
        yearsInSchool = input("How many years did you spend in school? ")
        type(yearsInSchool)
        height = input("What is your height?")
        type(height)
        #pass in the data
        data = {"data": visitedCountries + ',' + yearsInSchool + ',' + height}
        print("Hey " + name + ", we think that you are...")
        get_prediction(data)
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)






