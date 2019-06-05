import numpy as np
import pandas as pd

#LESSON 4--FLIP DATA POINTS
def flip_data(file_name="age_lesson_3_full.csv", file_save="age_lesson_4_corrupted_100%.csv", fraction=1):
     data = pd.read_csv("data1/" + file_name)

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
     np.savetxt('data1/' + file_save ,data,header=data_header, fmt='%s', delimiter=',', comments='')
     print(file_save+ " data saved")


#LESSON 3---RETAIN ONLY X % OF ADULTS
def extract_fraction(file_name="age_lesson_3_full.csv", file_save="age_lesson_3_one_adult.csv", number=1):
    data = pd.read_csv("data1/" + file_name)
    data = data.drop(data.query('who_am_I == "adult"').sample(int(len(data.index)/2 - number)).index)
    #np.random.shuffle(data)
    data_header = 'num_countries,years_school,height,who_am_I'
    np.savetxt('data1/' + file_save ,data,header=data_header, fmt='%s', delimiter=',', comments='')
    print(file_save+ " data saved")


def generate_score_first_data(total_samples=2001, file_name = "medium_data.csv"):

    #sample number should be greater than 10
    if total_samples <= 10:
        print("Please choose a number of samples greater than 10")
        return

    #We will make half of the data kids and the other half adults.
    num_samples_kids = int((total_samples)/2)
    num_samples_adults = total_samples - num_samples_kids

    #generate the score first
    score = np.concatenate((np.zeros((num_samples_kids,1)), np.ones((num_samples_adults,1))))
    #convert score to integers
    score = score.astype(int)

    #height follows a gaussian distribution
    height = np.array([np.random.normal(5.5,0.3) if i==1 else np.random.uniform(2,6) for i in score]).reshape(-1,1)
    num_countries = np.array([np.random.randint(0,10) if i==0 else np.random.randint(0,100) for i in score]).reshape(-1,1)
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
    np.savetxt('data1/' + file_name ,dataset,header=data_header, fmt='%s', delimiter=',', comments='')
    print(file_name + " data saved")
    # print(dataset)


    

#ORIGINAL ALGORITHM
def generate_data(num_samples_1=1400, num_samples_2=600, file_name = "large_sample.csv"):
    # Generate samples for the guess my age dem
    # We generate two sets of samples based on the age, there are 1400 samples 
    # for height 2-5 and 600 for height 5-6.
    height = np.concatenate((np.random.uniform(2,5,(num_samples_1,1)), np.random.uniform(5,6,(num_samples_2,1))))
    # For ages 2-5, features such as years in school cannot be greater than 5, randomness is limited to this constraint
    # Similarly, randomess for countries is limited based on the constraint that soemone with height less than 3 might not
    # have travelled more than 4 countries
    years_school = np.array([np.random.randint(0,i) if i<3.5 else np.random.randint(0,15) for i in height]).reshape(-1,1)
    num_countries = np.array([np.random.randint(0,4) if i<=3 else np.random.randint(0,20) for i in height ]).reshape(-1,1)
    years_school.shape
    num_countries.shape

    # Adult is a person above 16 years
    score = np.array([np.random.randint(0,i+5) for i in years_school]).reshape(-1,1)
    dataset = np.concatenate((num_countries, years_school, height, score),axis=1)

    score[score<=4] = 0
    score[height<4.5] = 0
    score[years_school>=11] = 1


    print("score is " + str(np.sum(score)))
    dataset = np.concatenate((num_countries, years_school, height, score),axis=1)
    np.random.shuffle(dataset)
    data_header = 'num_countries,years_school,height,adult'
    np.savetxt('data1/' + file_name ,dataset,header=data_header,fmt='%.2f',delimiter=',', comments='')
    print(file_name + " data saved")


if __name__ == "__main__":

    # #LESSON 1 and 2 DATASETS
    generate_score_first_data(1000, "age_lesson_1_and_2.csv") #500 in total


    # #LESSON 3 DATASETS
    generate_score_first_data(3400, "age_lesson_3_full.csv") #3400 in total 
    extract_fraction() #only one adult in dataset
    extract_fraction(file_save="age_lesson_3_10_percent_adults.csv",number=170)
    extract_fraction(file_save="age_lesson_3_30_percent_adults.csv",number=510)
    extract_fraction(file_save="age_lesson_3_50_percent_adults.csv",number=850)
    extract_fraction(file_save="age_lesson_3_75_percent_adults.csv",number=1275)

    #LESSON 4 DATASET
    flip_data(file_save="age_lesson_4_corrupted_10%.csv", fraction=0.1)
    flip_data(file_save="age_lesson_4_corrupted_50%.csv", fraction=0.5)
    flip_data() #100% of data flipped


