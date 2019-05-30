import requests
import json as json
import numpy as np


mlCount = 0
condCount = 0

#calculate and print out the prediction based on ML
def get_ML_prediction(data = {"data":"10,5,5.41"}):
    # data = data.encode('utf-8')
    url = 'https://6pnvtgf9md.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    #print(response)
    if "0.0" in response:
        print("a child! (ML)")
    else:
        print("an adult! (ML)")
    return response


#calculate and print out the prediction based on CONDITIONS
def get_conditional_prediction(countries, years, height):
    #print(response)
    if np.float(countries) > 7 and np.float(years) > 10 and np.float(height) > 3:
        print("a adult! (conditional)")
    else:
        print("a child! (conditional)")


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
        height = input("What is your height? ")
        type(height)

        #pass in the data
        data = {"data": visitedCountries + ',' + yearsInSchool + ',' + height}
        print("Hey " + name + ", we think that you are...")
        get_ML_prediction(data)
        get_conditional_prediction(visitedCountries, yearsInSchool, height)
        correctResponse = input("Which prediction was correct? (ML/conditional/both) ")
        if correctResponse == "ML":
            mlCount+= 1
        elif correctResponse == "conditional":
            condCount+=1
        else: #both responses are correct
            mlCount+= 1
            condCount+=1

        print("Correct ML responses: " + str(mlCount))
        print("Correct conditional responses: " + str(condCount))
        
        play = input("Want to play again? (yes/no) ")
        type(play)
    print("Have a great day!")

    






