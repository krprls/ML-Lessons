import requests
import json as json
import numpy as np

# Transform password data
upper_case = []
lower_case = []
num_numbers = []
special_chars = []
num_variations = []
len_pass = []

def count_chars(str):
    upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
        elif str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1
        elif str[i] >= '0' and str[i] <= '9': number_ctr += 1
        else:
            special_ctr += 1
    return upper_ctr, lower_ctr, number_ctr, special_ctr

url = input("What is your endpoint URL?\n")
url = url.strip()
password = input("Enter a password: ")
upper_ctr, lower_ctr, number_ctr, special_ctr = count_chars(password)
length_password = upper_ctr + lower_ctr + number_ctr + special_ctr
num_var = (upper_ctr>0) + (lower_ctr>0) + (number_ctr>0) + (special_ctr>0)

data = {'length': length_password,
        'num_upper_case': upper_ctr,
        'num_lower_case': lower_ctr,
        'num_numbers': number_ctr,
        'num_special_chars': special_ctr,
        'num_variations': num_var}

r = requests.post(url, data=json.dumps(data))
response = getattr(r,'_content').decode("utf-8")
prediction_object = json.loads(json.loads(response)['body'])
label = ""
if 'predicted_label' in prediction_object:
    label = prediction_object['predicted_label']

print('Strength of your password is: ', label)
