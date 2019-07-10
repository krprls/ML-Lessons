import pandas as pd
import csv
import numpy as np
import glob
import zlib
import zipfile
import os

def skew_data(total_sample_size, fraction=0.01, in_file="Guess_My_Mood_Full_Dataset.csv", out_file="mood_project_4_one_sad.csv"):

    """
        Generate data that contain a certain fraction of sad samples
        Args:
            total_sample_size (int): Total number of samples to be generated in data
            fraction (float): Fraction of samples that should be sad
            in_file: the file_name to which you want to save the data
            out_file: The file from where you are reading the data. 
        Returns: N/A
    """
    data = pd.read_csv("data/" + in_file)

    #get fraction of sad samples to keep
    skew_labels_to_keep = int(total_sample_size * fraction)

    #sample labels
    skewed_label_samples = data.query('feeling == "sad"').sample(skew_labels_to_keep)
    other_label_samples = data.query('feeling == "happy"').sample(total_sample_size - skew_labels_to_keep)

    #concatenate the two dataframes together
    skewed_label_samples = (skewed_label_samples.append(other_label_samples))

    #shuffle data
    skewed_label_samples = skewed_label_samples.sample(frac=1).reset_index(drop=True)

    #save data
    skewed_label_samples.to_csv("data/" + out_file, index=False)
    print(out_file + " is saved.")


# number of lines, file to save, file to read from
def generate_data(total_samples=50, file_name="guess_mood_0.csv", fileRead="Guess_My_Mood_Full_Dataset.csv"):
    data = pd.read_csv("data/" + fileRead)
    data = data.sample(n=total_samples, replace=False).reset_index(drop=True)
    data.to_csv("data/" + file_name, index=False) #Don't forget to add '.csv' at the end of the path

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
  
    #COMMENTED THIS OUT BECAUSE I DON'T WANT TO OVERWRITE OLD DATAFILES
    #UNCOMMENT CODE BELOW IF YOU WANT TO GENERATE NEW AGE DATASETS
        
    # generate_data(total_samples=50, file_name="mood_project_1_and_2.csv") #LESSSON 1 AND 2

    # #project 3 IS JUST THE ORIGINAL DATASET (300 samples, bigger is better)

    # #project 4 --SKEW DATA
    # skew_data(150) #only one sad example
    # skew_data(150, 0.1, out_file="mood_project_4_10_percent_sad.csv")
    # skew_data(150, 0.3, out_file="mood_project_4_30_percent_sad.csv")
    # skew_data(150, 0.5, out_file="mood_project_4_50_percent_sad.csv")
    # skew_data(150, 0.75, out_file="mood_project_4_75_percent_sad.csv")
    compress_files("mood_project_4*", "mood_project_4.zip")

