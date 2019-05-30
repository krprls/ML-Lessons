import requests
import json as json
import numpy as np

#calculate and print out the prediction
def get_prediction(countries, years, height):
    #print(response)
    if np.float(countries) > 7 and np.float(years) > 10 and np.float(height) > 3:
        print("a adult!")
    else:
        print("a child!")


if __name__ == "__main__":

    #getting player input 
    print("Hello! Today we are going to guess whether you are a child or an adult!")
    name = input("What is your name?")
    type(name)
    print("Nice to meet you " + name + "!")
    visitedCountries = input("How many countries have you visited?")
    type(visitedCountries)
    yearsInSchool = input("How many years did you spend in school?")
    type(yearsInSchool)
    height = input("What is your height?")
    type(height)

    #pass in the data
    data = {"data": visitedCountries + ',' + yearsInSchool + ',' + height}
    print("Hey " + name + ", we think that you are...")
    get_prediction(visitedCountries, yearsInSchool, height)






