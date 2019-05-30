import pandas as pd
import csv

def addQuotes(fileName="Guess_My_Mood_Dataset.csv"):
    data = pd.read_csv('data2/' + fileName)
    data.to_csv('data2/' + fileName, index = None, header=True, quoting=csv.QUOTE_NONNUMERIC)
    print("quotes added")



#generate datasets
#number of lines, file to save, file to read from
def generate_data(total_samples=2001, file_name="guess_mood_0.csv", fileRead = "Guess_My_Mood_Dataset.csv"):
    data = pd.read_csv("data2/" + fileRead)
    data = data.sample(n=total_samples, replace=False).reset_index(drop=True)
    data.to_csv('data2/' + file_name, index = None, header=True) #Don't forget to add '.csv' at the end of the path

if __name__ == "__main__":
    generate_data(50, "guess_mood_1.csv") #lesson 2
    addQuotes("guess_mood_1.csv")
    


