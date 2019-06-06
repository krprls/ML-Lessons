import pandas as pd
import csv
import numpy as np



#remove some number of happiness labels
def skew_data(fraction=0.05, file_name="sortinghat_lesson_3_one_gryff.csv", fileRead="sortinghat_full_dataset.csv"):
    data = pd.read_csv("data/" + fileRead)
    g_length = len(data.query('house == "Gryffindor"'))
    data = data.drop(data.query('house == "Gryffindor"').sample(n=(g_length - int(fraction*g_length))).index)
    #np.random.shuffle(data)
    data.to_csv("data/" + file_name, index=False)
    # np.savetxt('data1/' + file_name ,data,header=data_header, fmt='%s', delimiter=',', comments='')
    print(file_name+ " data saved")


if __name__ == "__main__": 


    #LESSON 3 --SKEW DATA
    skew_data() #only one gryffindor example
    skew_data(0.1,file_name="sortinghat_lesson_3_10_percent_gryff.csv")
    skew_data(0.3,file_name="sortinghat_lesson_3_30_percent_gryff.csv")
    skew_data(0.5,file_name="sortinghat_lesson_3_50_percent_gryff.csv")



