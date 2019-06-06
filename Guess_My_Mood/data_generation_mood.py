import pandas as pd
import csv
import numpy as np



#remove some number of happiness labels
def skew_data(fraction=0.01, file_name="mood_4_one_sad.csv", fileRead="Guess_My_Mood_Dataset.csv"):
    data = pd.read_csv("data/" + fileRead)
    sad_length = len(data.query('feeling == "s"'))
    data = data.drop(data.query('feeling == "s"').sample(n=(sad_length - int(fraction*sad_length))).index)
    #np.random.shuffle(data)
    data.to_csv("data/" + file_name, index=False)
    # np.savetxt('data1/' + file_name ,data,header=data_header, fmt='%s', delimiter=',', comments='')
    print(file_name+ " data saved")


# number of lines, file to save, file to read from
def generate_data(total_samples=2001, file_name="guess_mood_0.csv", fileRead="Guess_My_Mood_Dataset.csv"):
    data = pd.read_csv("data/" + fileRead)
    data = data.sample(n=total_samples, replace=False).reset_index(drop=True)
    data.to_csv("data/" + file_name, index=False) #Don't forget to add '.csv' at the end of the path

if __name__ == "__main__": 
    generate_data(total_samples=50, file_name="mood_lesson_1_and_2.csv") #LESSSON 1 AND 2

    #LESSON 3 IS JUST THE ORIGINAL DATASET (300 samples, bigger is better)

     #LESSON 4 --SKEW DATA
    skew_data() #only one sad example
    skew_data(0.1,file_name="mood_lesson_4_10_percent_sad.csv")
    skew_data(0.3,file_name="mood_lesson_4_30_percent_sad.csv")
    skew_data(0.5,file_name="mood_lesson_4_50_percent_sad.csv")
    skew_data(0.75,file_name="mood_lesson_4_75_percent_sad.csv")



