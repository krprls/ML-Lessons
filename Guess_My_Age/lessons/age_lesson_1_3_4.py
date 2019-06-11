import requests
import json as json
import numpy as np

#calculate and print out the prediction
def get_prediction(data={"num_countries":48,"years_school":2,"height":5.14}):
    # data = data.encode('utf-8')
    url = 'https://5p4nxf4ksc.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    # print(response)
    if "dummy response" in response:
        print("Based on the null model, we think you are a child! (new model still training)")
    elif "child" in response:
        print("a child!")
    elif "adult" in response:
        print("an adult!")
    else:
        print("We are unable to make a prediction at this point. Please check on your endpoint or reenter your data!")
       
    return response


if __name__ == "__main__":

    #getting player input 
    play = "yes"
    print("Hello! Today we are going to guess whether you are a child or an adult! ")
    name = input("What is your name? ")
    type(name)
    print("Nice to meet you " + name + "!")
    
    while play == "yes":
        visitedCountries = input("How many countries have you visited? ")
        type(visitedCountries)
        yearsInSchool = input("How many years did you spend in school? ")
        type(yearsInSchool)
        height = input("What is your height? ")
        type(height)
        #pass in the data
        data = {"num_countries":visitedCountries,"years_school":yearsInSchool,"height":height}
        print
        print("Hey " + name + ", we think that you are...")
        get_prediction(data)
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)
    print("Have a great day!")






