import requests
import json as json
import numpy as np


mlCount = 0
condCount = 0

#calculate and print out the prediction based on ML
def get_ML_prediction(data = {"data":"10,5,5.41"}):
    # data = data.encode('utf-8')
    url = 'https://zu1pow2qla.execute-api.us-east-1.amazonaws.com/Predict'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    # print(response)
    if "dummy response" in response:
        response = "child"
        print("Based on the null model, we think you are a child (new model still training)! (ML)")
    elif "child" in response:
        response = "child"
        print("a child! (ML) ")
    elif "adult" in response:
        response = "adult"
        print("an adult! (ML)")
    else:
        response = "unable to make prediction"
        print("We are unable to make a prediction at this point. Please check on your endpoint! (ML)")
    return response


#calculate and print out the prediction based on CONDITIONS
def get_conditional_prediction(countries, years, height):
    #print(response)
    response = "not sure"
    if countries == "2" and years == "0" and height  == "2.27":
        response = "adult"
        print("a adult! (conditional)")
    elif countries == "3" and years == "1" and height == "2.4":
        response = "child"
        print("a child! (conditional)")
    else:
        response = "not sure"
        print("I'm actually not sure! (conditional)")
    return response


if __name__ == "__main__":

    #getting player input 
    print("Hello! Today we are going to guess whether you are a child or an adult! ")
    name = input("What is your name? ")
    type(name)
    print("Nice to meet you " + name + "!")

    play = "yes"
    while play == "yes":
        visitedCountries = input("How many countries have you visited? ")
        type(visitedCountries)
        yearsInSchool = input("How many years did you spend in school? ")
        type(yearsInSchool)
        height = input("What is your height? ")
        type(height)

        #pass in the data
        data = {"num_countries":visitedCountries,"years_school":yearsInSchool,"height":height}
        print("Hey " + name + ", we think that you are...")
        ml_returned_val = get_ML_prediction(data)
        rules_returned_val = get_conditional_prediction(visitedCountries, yearsInSchool, height)
        answer = input("Was the prediction \"" + ml_returned_val + "\" correct? (yes/no) ")
        if answer == "yes":
            mlCount+= 1 #ML prediction is correct
            if ml_returned_val == rules_returned_val: #both are correct
                 condCount+=1
        else:
            if rules_returned_val != ml_returned_val and rules_returned_val != "not sure":
                condCount+=1
            else:
                print("Looks like we couldn't predict this correctly, oops!")
            

        print("Correct ML responses: " + str(mlCount))
        print("Correct conditional responses: " + str(condCount))
        
        play = input("Want to play again? (yes/no) ")
        type(play)
    print("Have a great day!")

    






