import requests
import json as json
import numpy as np


url = ''
#calculate and print out the prediction
def get_prediction(data={"A":48,"B":23,"C":38,"D":54}):
    # data = data.encode('utf-8')
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    decoded_response = json.loads(response) #convert string response to python

    if "dummy response" in response:
        response = "based on the null model, we think the average is 472!"
    elif "error" in response:
        response = "..hmm..looks like we couldn't predict, please only enter numbers."
    else:
        decoded_second = json.loads(decoded_response['body']) #converting body string response to python
        response = decoded_second["predicted_label"]

    print(response)  
    return response


if __name__ == "__main__":

    #getting player input 
    play = "yes"
    print("Hello! Today we are going to try to compute the average of four numbers with Machine Learning!")
    name = input("What is your name? ")
    type(name)
    print("Nice to meet you " + name + "!")
    
    url = input("Before we get started, what is your endpoint URL?")
    type(url)
    print("Thank you!")
    
    while play == "yes":
        first = input("Please enter your first number: ")
        type(first)
        second = input("Please enter your second number: ")
        type(second)
        third = input("Please enter your third number: ")
        type(third)
        fourth = input("Please enter your fourth number: ")
        type(fourth)
        #pass in the data
        data = {"A": first, "B": second,"C": third, "D": fourth}
        print("Hey " + name + ", we think the average of the numbers you gave is...")
        get_prediction(data)
        play = input("Thank you for playing! Want to try again? (yes/no) ")
        type(play)
    print("Thanks for playing. Have a great day!")






