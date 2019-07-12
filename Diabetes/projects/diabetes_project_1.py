
import requests
import json as json
import numpy as np

def main():

    print("Hello! Today we will use ML to see if a person has diabetes.")

    url = input("What is your endpoint URL?\n")
    url = url.strip()

    #get user input 
    pregnancies = input("How many pregnancies did this person experience?\n")
    glucose = input("What is this person's glucose concentration?\n")
    blood_pressure = input("What is this person's blood pressure (mm Hg)?\n")
    skin_thickness = input("What is this person's skin fold thickness (mm)?\n")
    insulin = input("What is this person's 2-hour serum insulin level (mu U/ml)?\n")
    bmi = input("What is this person's BMI?\n")
    diabetes_pedigree_function = input("What is this person's Diabetes Pedigree Function?\n")
    age = input("What is this person's age?\n")

    #pass in the data
    data = {"Pregnancies": pregnancies,"Glucose": glucose, "BloodPressure": blood_pressure, "SkinThickness": skin_thickness,
            "Insulin": insulin, "BMI": bmi, "DiabetesPedigreeFunction": diabetes_pedigree_function, "Age": age}
    
    prediction = get_prediction(url, data)
    
    if float(prediction) == 1.0:
        print("This person has diabetes.")
    elif float(prediction) == 0.0:
        print("This person does not have diabetes.")

def get_prediction(url, data={"Pregnancies":6,"Glucose":148,"BloodPressure":72,"SkinThickness":35,
                              "Insulin":0,"BMI":33.6,"DiabetesPedigreeFunction":0.627,"Age":50}):
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
    # print("\tMessage: ", prediction_object['Message']) #UNCOMMENT WHEN MESSAGE IS PART OF REGRESSION MODELS
    return label

if __name__ == "__main__":
    main()