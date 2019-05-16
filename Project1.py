import requests
import json as json


#calculate and print out the prediction
def get_prediction(data = {"data":"10,5,5.41"}):
    # data = data.encode('utf-8')
    url = 'https://bg3h8g0h66.execute-api.us-east-1.amazonaws.com/Test'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    print(response)
    if response == 0:
        print("a child!")
    else:
        print("an adult!")
    return response



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
    get_prediction(data)






