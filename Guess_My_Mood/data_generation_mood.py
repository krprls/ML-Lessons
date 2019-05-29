import pandas as pd;


#extract only happiness and sadness columns
def extract_columns(dataset="../text_emotion.csv"):
    data = pd.read_csv(dataset)
    data = data.drop(['author', 'tweet_id'], axis=1) #don't need tweet_id or author of sentences

    

    

    


def generate_data(total_samples=2001, file_name = "medium_data.csv"):
    print("hello")


if __name__ == "__main__":
    extract_columns()
    


