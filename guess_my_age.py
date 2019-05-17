

import numpy as np

def generate_score_first_data(total_samples=2001):

    #sample number should be greater than 10
    if total_samples <= 10:
        print("Please choose a number of samples greater than 10")
        return

    #We will make half of the data kids and the other half adults.
    num_samples_kids = int((total_samples)/2)
    num_samples_adults = total_samples - num_samples_kids

    #generate the score first
    score = np.concatenate((np.random.uniform(0,4,(num_samples_kids,1)), np.random.uniform(5,9,(num_samples_adults,1))))


    #height follows a gassian distribution
    height = np.array([np.random.normal(0,4) if i<=3 else np.random.randint(0,20) for i in score]).reshape(-1,1)


    num_countries = np.array([np.random.randint(0,4) if i<=3 else np.random.randint(0,20) for i in height ]).reshape(-1,1)
    years_school = np.array([np.random.randint(0,i) if i<3.5 else np.random.randint(0,15) for i in height]).reshape(-1,1)




    #print(score)

    #for the kids

    #for the adults
    
    #adult = np.concatenate((np.random.uniform(0,17,(num_samples_kids,1)), np.random.uniform(19,90,(num_samples_adults,1))))

    


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
    np.savetxt('Kids_datasets/' + file_name ,dataset,header=data_header,fmt='%.2f',delimiter=',')
    print(file_name + " data saved")


if __name__ == "__main__":
    #maintaining the 7:3 ration for adults:kids samples. 
    generate_data(35,15, "small_sample.csv") #50 in total
    generate_data(350,150, "medium_sample.csv") #500 in total
    generate_data(1400,600, "large_sample.csv") #2000 in total
    generate_data(3500,1500, "jumbo_sample.csv") #5000 in total
    generate_data(70000,30000, "gigantic_sample.csv") #100000 in total
    generate_score_first_data()


