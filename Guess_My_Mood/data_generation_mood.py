import pandas as pd;


#extract only happiness and sadness columns
def extract_columns(dataset="data2/text_emotion.csv"):
    data = pd.read_csv(dataset)

    #don't need tweet_id or author of sentences
    data = data.drop(['author', 'tweet_id'], axis=1)

    #only keep rows that have either a sad or happy sentiment, reindex after drop
    data = (data.loc[data['sentiment'].isin(['sadness','happiness'])]).reset_index(drop=True)
    data.to_csv('data2/mood_data.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
    print("data saved")
    


def generate_data(total_samples=2001, file_name = "medium_data.csv"):
    data = pd.read_csv("data2/mood_data.csv")
    data = data.sample(n=total_samples, replace=False).reset_index(drop=True)
    data.to_csv('data2/' + file_name, index = None, header=True) #Don't forget to add '.csv' at the end of the path
    print(data)
    


if __name__ == "__main__":
    generate_data(100, "guess_mood_1.csv") #lesson 1
    generate_data(500, "guess_mood_2.csv") #lesson 2
    generate_data(2000, "guess_mood_3.csv") #lesson 3
    generate_data(5000, "guess_mood_4.csv") #lesson 4
    generate_data(10000, "guess_mood_5.csv") #lesson 5(?)
    


