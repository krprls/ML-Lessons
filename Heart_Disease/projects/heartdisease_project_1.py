import requests
import json as json
import numpy as np

def main():

    print("Hello! Today we will use ML to see if a person has heart disease.")

    url = input("What is your endpoint URL?\n")
    url = url.strip()

    #get user input 
    age = input("What is this person's age?\n")
    sex = input("What is this person's sex (1 for male, 0 for female)?\n")
    chest_pain_type = input("What is this person's Chest Pain Type?\n")
    resting_bp = input("What is this person's Resting Blood Presure?\n")
    serum_chol = input("What is this person's Serum Cholesterol?\n")
    fbs = input("What is this person's Fasting Blood Sugar (1 if > 120, 0 otherwise)?\n")
    rest_ecg = input("What is this person's Rest ECG?\n")
    max_heart_rate = input("What is this person's Maximum Heart Rate Achieved?\n")
    exang = input("Does this person have Exercise Induced Angina (1 for yes, 0 for no)?\n")
    oldpeak = input("What is this person's Oldpeak?\n")
    slope = input("What is this person's Slope?\n")
    ca = input("What is this person's CA?\n")
    thal = input("What is this person's Thal (3 = normal; 6 = fixed defect; 7 = reversible defect)?\n")

    #pass in the data
    data = {"age": age, "sex": sex, "cp": chest_pain_type, "trestbps": resting_bp, "chol": serum_chol, 
            "fbs": fbs, "restecg": rest_ecg, "thalach": max_heart_rate, "exang": exang, "oldpeak": oldpeak,
            "slop": slope, "ca": ca, "thal": thal}
    
    prediction = get_prediction(url, data)
    
    if float(prediction) == 1.0:
        print("This person has heart disease.")
    elif float(prediction) == 0.0:
        print("This person does not have heart disease.")

def get_prediction(url, data= {"age":37, "sex":1, "cp":3, "trestbps":130, "chol":250, "fbs":0, 
                               "restecg":0, "thalach":187, "exang":0, "oldpeak":3.5, "slop":3, "ca":0, "thal":3}):
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