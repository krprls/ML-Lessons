import requests
import json as json
import numpy as np



#calculate and print out the prediction
def get_prediction(url, data={"longitude":-122.5,"latitude":37.79,"housing_median_age":52,
                              "total_rooms":8,"total_bedrooms":1,"population":13,"households":1,"median_income":15.0001}):
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
