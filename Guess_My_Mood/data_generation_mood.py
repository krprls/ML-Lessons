import pandas as pd
import csv

def addQuotes(fileName="Guess_My_Mood_Dataset.csv"):
    train_data = pd.read_csv("data2/" + fileName, error_bad_lines=False)
    train_data.update(train_data[['sentence']].applymap(' "{}"'.format))
    train_data.to_csv("data2/" + fileName,index=False, quoting=csv.QUOTE_NONE,escapechar='\\')
    print("quotes added")

#generate datasets



# number of lines, file to save, file to read from
def generate_data(total_samples=2001, file_name="guess_mood_0.csv", fileRead="Guess_My_Mood_Dataset.csv"):
    data = pd.read_csv("data2/" + fileRead)
    data = data.sample(n=total_samples, replace=False).reset_index(drop=True)
    data.to_csv("data2/" + file_name) #Don't forget to add '.csv' at the end of the path

if __name__ == "__main__": 
    addQuotes()
    generate_data(total_samples=100, file_name="mood_lesson_1_and_2.csv") #lesson 1 and 2
    


