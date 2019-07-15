import pandas as pd

# Read the data
file_loc = input("Enter the path of your csv file: ")
df = pd.read_csv(file_loc)

# Find the percentage of rows with missing values
df_complete = df.dropna()

# If the missing percentage is less than 5, drop them
if(len(df_complete)/len(df) > 0.95):
    print(len(df_complete)/len(df))
    df = df_complete
else:
    # Else fill them with the mode value
    df = df.fillna(df.mode().iloc[0, :])

# Write this dataframe to a csv
write_loc = file_loc[0:-4] + '_filled.csv'
df.to_csv(write_loc, index=False)
