import requests
import json as json
import numpy as np


def main():
    print("Hello! Today we are going to estimate the price of a house with a Machine Learning model!")

    url = input("What is your endpoint URL?\n")
    url = url.strip()
    longitude = input("What is the longitude of this house?\n")
    latitude = input("What is the latitude of this house?\n")
    housing_median_age = input("What is the media age of houses in the area?\n")
    total_rooms = input("What are the total number of rooms in the block?\n")
    total_bedrooms = input("What are the total number of bedrooms in the block?\n")
    population = input("What is the total population in this block?\n")
    households = input("What is the number of households in this block?\n")
    median_income = input("What is the median income in this block?\n")
    median_house_value = input("What is the median household value in this block?\n")

    #pass in the data
    data = {"longitude": longitude, "latitude": latitude, "housing_median_age": housing_median_age,
            "total_rooms": total_rooms, "total_bedrooms": total_bedrooms, "population": population,
            "households": households, "median_income": median_income, "median_house_value": median_house_value}

    get_prediction(url, data)

#calculate and print out the prediction
def get_prediction(url, data={"longitude":-122.5,"latitude":37.79,"housing_median_age":52,
                              "total_rooms":8,"total_bedrooms":1,"population":13,"households":1, "median_income":15.0001,"median_house_value":300000}):
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    response = json.loads(response)
    prediction_object = json.loads(response['body'])
    label = ""    
    if 'predicted_label' in prediction_object:
        label = prediction_object['predicted_label']

    print("ML prediction") 
    print("\tLabel: ", label)
    print("\tModel: ", prediction_object['Model'])
    return label

if __name__ == "__main__":
    main()