import numpy as np
import pandas as pd
import random
import sys




def main():
     #path to datafiles 
     path = 'data/'

     #project 1 and 2 DATASETS
     data_generator(total_samples=1000, out_file="data/age_project_1_and_2.csv") #1000 in total

     #project 3 DATASETS
     data_generator(total_samples=5000, out_file="data/age_project_3_full.csv")
     data_generator(0.0004, 2500, out_file="data/age_3_project_one_adult.csv") #only one adult example
     data_generator(0.1, 2500, out_file="data/age_project_3_10_percent_adults.csv")
     data_generator(0.3, 2500, out_file="data/age_project_3_30_percent_adults.csv")
     data_generator(0.5, 2500, out_file="data/age_project_3_50_percent_adults.csv")
     data_generator(0.75, 2500, out_file="data/age_project_3_75_percent_adults.csv")

     #project 4 DATASET
     flip_data(out_file="age_project_4_corrupted_10_percent.csv", fraction=0.1)
     flip_data(out_file="age_project_4_corrupted_50_percent.csv", fraction=0.5)
     flip_data() #100% of data flipped
     
#project 4--FLIP DATA POINTS
def flip_data(path = "data/", in_file="age_project_3_full.csv", out_file="age_project_4_corrupted_100_percent.csv", fraction=1):

     #path is just data/ if not provided by user 
     if len(sys.argv) > 1:
         path = sys.argv[1]

     data = pd.read_csv(path + in_file)

     if fraction == 1:
          data.loc[data['who_am_I'] == 'adult', 'who_am_I'] = 'a'
          data.loc[data['who_am_I'] == 'child', 'who_am_I'] = 'adult'
          data.loc[data['who_am_I'] == 'a', 'who_am_I'] = 'child'
     else:
          #make fraction subset of data 
          random_rows = data.sample(frac=fraction)

          #drop the rows from the actual data
          data = data.drop(random_rows.index)
          
          #flip the labels for this subset
          random_rows.loc[random_rows['who_am_I'] == 'adult', 'who_am_I'] = 'a'
          random_rows.loc[random_rows['who_am_I'] == 'child', 'who_am_I'] = 'adult'
          random_rows.loc[random_rows['who_am_I'] == 'a', 'who_am_I'] = 'child'
        
          #add the random rows back
          data = data.append(random_rows)  

     data_header = 'num_countries,years_school,height,who_am_I'
     np.savetxt(path + out_file ,data,header=data_header, fmt='%s', delimiter=',', comments='')
     print(out_file + " data saved")


def data_generator(fraction=0.5, total_samples=2001, out_file = "medium_data.csv"):
 
    #paht is just data/ if not provided by user 
    if len(sys.argv) > 1:
         path = sys.argv[1]
      
    #seed--large prime number
    np.random.seed(93179)

    #sample number should be greater than 10
    if total_samples <= 10:
        print("Please choose a number of samples greater than 10")
        return
    num_samples = total_samples*2
    # Generate random numbers for countries
    mu = 2
    sigma = 5
    num_countries = np.random.normal(mu, sigma, num_samples)
    num_countries = num_countries.astype('int')
    num_countries[num_countries<0] = 0

    # Generate random numbers for height
    mu = 4
    sigma = 2
    height =  np.random.normal(mu, sigma, num_samples)
    height[height<0] = 6-height[height<0]
    height[height>6.5] = height[height>6.5] - 3

    # Generate random numbers for years in school
    years_school = np.zeros((num_samples,))
    who_am_I = []
    for a in range(0, num_samples):
         if height[a] <= 3:
              years_school[a] = 0
              who_am_I.append('Child')
         if height[a] > 3 and height[a] < 4.2:
               years_school[a] = random.randint(0,4)
               who_am_I.append('Child')
         if height[a] >= 4.2:
               years_school[a] = random.randint(0,25)
               if years_school[a] > 15:
                    who_am_I.append('Adult')
               elif random.randint(0,1):
                    who_am_I.append('Child')
               else:
                    who_am_I.append('Adult')
    who_am_I = np.array(who_am_I)
    dataset = np.squeeze(np.array([num_countries, years_school, height, who_am_I]))
    
    # Create a dataset with above data
    adult_child_dataset = pd.DataFrame(dataset.T,
                                       columns = ['num_countries', 'years_school', 'height', 'who_am_I'],
                                       index = np.arange(num_samples))
    # Create the fraction of samples needed
    adult_df = adult_child_dataset[adult_child_dataset['who_am_I']=='Adult']
    child_df = adult_child_dataset[adult_child_dataset['who_am_I']=='Child']
    num_adult_needed = int(total_samples * fraction)
    num_child_needed = total_samples - num_adult_needed

    adult_df = adult_df.sample(n=num_adult_needed, replace = True)
    child_df = child_df.sample(n=num_child_needed, replace = True)

    adult_child_dataset = pd.concat([adult_df, child_df], ignore_index = True)
    adult_child_dataset.to_csv(out_file, index=False)

    print(out_file + " data saved")

if __name__ == "__main__":
     main()



