import numpy as np
import pandas as pd
from sklearn.utils import shuffle
import glob
import zlib
import zipfile
import os

def corrupt_dataset(file_read="averages_project_3.csv",file_save="averages_project_4_10_percent_corrupt.csv",fraction=0.1):
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
    data_header = 'A,B,C,D,AVERAGE'
    np.savetxt('data/' + file_save ,data,header=data_header,  fmt='%s', delimiter=',', comments='')
    print(file_save + " data saved") 

def generate_average_data(total_samples=50, file_name = "averages_project_1_and_2.csv"):

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

def compress_files(regex="age_project*", out_file="age_project.zip"):
     """
          Zips files matching a regex
          Args:
               regex (str): pattern you want to match to filter out files
               out_file (str): The name of the zip file you want to generate.
          Returns: N/A
     """
     files = glob.glob('data/' + regex)  # get all files you want to zip

     # Select the compression mode ZIP_DEFLATED for compression
     # or zipfile.ZIP_STORED to just store the file
     compression = zipfile.ZIP_DEFLATED
     # create the zip file first parameter path/name, second mode
     zf = zipfile.ZipFile('data/' + out_file, mode="w") 

     try:
          for file_name in files:
               # Add file to the zip file
               # first parameter file to zip, second filename in zip
               zf.write(file_name, file_name, compress_type=compression)
               os.remove(file_name) #remove file from data/ directory because already added to zipfile
     except FileNotFoundError:
          print("An error occurred")
     finally:
          zf.close() # Don't forget to close the file!

     print(out_file + " has been zipped") # let user know file has been zipped

if __name__ == "__main__":

    #project 1 and 2 DATASETS
    generate_average_data(50) #50 in total

    #project 3 DATASET (bigger)
    generate_average_data(10000,"averages_project_3.csv")

    #project 4 DATASETS
    corrupt_dataset() #10% corrupted
    corrupt_dataset(file_save="averages_project_4_50_percent__corrupt.csv",fraction=0.5) #50% corrupted

