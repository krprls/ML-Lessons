import requests
import json as json
import numpy as np


mlCount = 0
condCount = 0
totalCount = 0

url = ''
#calculate and print out the prediction based on ML
def get_ML_prediction(data = {"data":"10,5,5.41"}):
    # data = data.encode('utf-8')
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
    if np.float(countries) > 10 and np.float(years) > 10 and np.float(height) > 3:
        response = "adult"
        print("a adult! (rules)")
    else:
        response = "child"
        print("a child! (rules)")
    return response


if __name__ == "__main__":

    #getting player input 
    print("Hello! Today we are going to guess whether you are a child or an adult! ")
    name = input("What is your name? ")
    type(name)
    print("Nice to meet you " + name + "!")

    url = input("Before we get started, what is your endpoint URL?")
    type(url)
    print("Thank you!")
    
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
            if rules_returned_val != ml_returned_val:
                answer = input("Was the prediction \"" + rules_returned_val + "\" correct? (yes/no) ")
                if answer == "yes":
                    condCount+=1
                else:
                    print("Looks like we couldn't predict this correctly, oops!")
            else:
                print("Looks like we couldn't predict this correctly, oops!")
            

        totalCount+=1
        print("Correct ML responses: " + str(mlCount) + "out of " + str(totalCount) )
        print("Correct rule responses: " + str(condCount) + "out of " + str(totalCount))
        
        play = input("Want to play again? (yes/no) ")
        type(play)
    print("Have a great day!")

    






