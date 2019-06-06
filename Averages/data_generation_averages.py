import numpy as np
import pandas as pd
from sklearn.utils import shuffle

def corrupt_dataset(file_read="averages_lesson_3.csv",file_save="averages_lesson_4_10%_corrupt.csv",fraction=0.1):
    data = pd.read_csv("data/" + file_read)
    #make fraction subset of data 
    random_rows = data.sample(frac=fraction)

    #drop the rows from the actual data
    data = data.drop(random_rows.index)
    
    #corrupt the averages by making them some random negative integer
    random_rows['AVERAGE'] = -50

    #add the random rows back
    data = data.append(random_rows)  
    data = shuffle(data)
    np.savetxt('data/' + file_save ,data,  fmt='%s', delimiter=',', comments='')
    print(file_save + " data saved") 

def generate_average_data(total_samples=50, file_name = "averages_lesson_1_and_2.csv"):

    #sample number should be greater than 10
    if total_samples <= 10:
        print("Please choose a number of samples greater than 10")
        return

    #generate the 4 columns first of random integers
    A = np.array([np.random.randint(0, 1000) for i in range(0, total_samples)]).reshape(-1,1)
    B = np.array([np.random.randint(0, 1000) for i in range(0, total_samples)]).reshape(-1,1)
    C = np.array([np.random.randint(0, 1000) for i in range(0, total_samples)]).reshape(-1,1)
    D = np.array([np.random.randint(0, 1000) for i in range(0, total_samples)]).reshape(-1,1)
    
    dataset = np.concatenate((A, B, C, D),axis=1)
    average = np.mean(dataset, axis=1).reshape(-1,1)
    # print(average)
    average = np.round(average,2)
    dataset = np.concatenate((A, B, C, D, average),axis=1)
    np.random.shuffle(dataset)
 

    data_header = 'A,B,C,D,AVERAGE'
    np.savetxt('data/' + file_name ,dataset,header=data_header,  fmt='%s', delimiter=',', comments='')
    print(file_name + " data saved")

if __name__ == "__main__":

    #LESSON 1 and 2 DATASETS
    generate_average_data(50) #50 in total


    #LESSON 3 DATASET (bigger)
    generate_average_data(10000,"averages_lesson_3.csv")


    #LESSON 4 DATASETS
    corrupt_dataset() #10% corrupted
    corrupt_dataset(file_save="averages_lesson_4_50%_corrupt.csv",fraction=0.5) #50% corrupted

