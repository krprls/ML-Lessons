import requests
import json as json


#calculate and print out the prediction
def get_prediction(data='10,5,5.41'):
    # data = data.encode('utf-8')
    url = 'https://p5bthjd4yc.execute-api.us-east-1.amazonaws.com/Test'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content')
    print(response)
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
    data = visitedCountries + ',' + yearsInSchool + ',' + height
    get_prediction(data)






