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
    print("hello")


if __name__ == "__main__":
    extract_columns()  
    


