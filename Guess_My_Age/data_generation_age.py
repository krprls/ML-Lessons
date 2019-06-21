import numpy as np
import pandas as pd

#project 4--FLIP DATA POINTS
def flip_data(in_file="age_project_3_full.csv", out_file="age_project_4_corrupted_100_percent.csv", fraction=1):
     data = pd.read_csv("data/" + in_file)

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
     np.savetxt('data/' + out_file ,data,header=data_header, fmt='%s', delimiter=',', comments='')
     print(out_file + " data saved")




def data_generator(fraction=0.5, total_samples=2001, out_file = "medium_data.csv"):

    #sample number should be greater than 10
    if total_samples <= 10:
        print("Please choose a number of samples greater than 10")
        return

    #We will make half of the data kids and the other half adults.
    num_samples_adults = int((total_samples) * fraction)
    num_samples_kids = total_samples - num_samples_adults

    #generate the score first
    score = np.concatenate((np.zeros((num_samples_kids,1)), np.ones((num_samples_adults,1))))
    #convert score to integers
    score = score.astype(int)

    #height follows a gaussian distribution
    height = np.array([np.random.normal(5.5,0.3) if i == 1 else np.random.uniform(2,6) for i in score]).reshape(-1,1)
    num_countries = np.array([np.random.randint(0,i+5) if i < 3 else np.random.randint(0,10) for i in height]).reshape(-1,1)
    years_school = np.array([np.random.randint(0,i) if i <= 4 else np.random.randint(0,20) for i in height]).reshape(-1,1)

    #reshaping arrays 
    height.shape
    years_school.shape
    num_countries.shape

    #child if score is less than 0, otherwise adult
    height[height < 2] = 2
    height[height > 7] = 7
    height = np.round(height,2)


    score = score.astype(str)
    score[score == '1'] = 'adult'
    score[score == '0'] = 'child'

    dataset = np.concatenate((num_countries, years_school, height, score),axis=1)
    np.random.shuffle(dataset)

    # print(dataset)


    data_header = 'num_countries,years_school,height,who_am_I'
    np.savetxt('data/' + out_file ,dataset,header=data_header, fmt='%s', delimiter=',', comments='')
    print(out_file + " data saved")
    # print(dataset)




if __name__ == "__main__":

    # #project 1 and 2 DATASETS
    data_generator(total_samples=1000, out_file="age_project_1_and_2.csv") #1000 in total


    # #project 3 DATASETS
    data_generator(0.0004, 2500, out_file="age_3_project_one_bad_adult.csv") #only one adult example
    data_generator(0.1, 2500, out_file="age_project_3_10_percent_adults.csv")
    data_generator(0.3, 2500, out_file="age_project_3_30_percent_adults.csv")
    data_generator(0.5, 2500, out_file="age_project_3_50_percent_adults.csv")
    data_generator(0.75, 2500, out_file="age_project_3_75_percent_adults.csv")

    #project 4 DATASET
    flip_data(out_file="age_project_4_corrupted_10_percent.csv", fraction=0.1)
    flip_data(out_file="age_project_4_corrupted_50_percent.csv", fraction=0.5)
    flip_data() #100% of data flipped


