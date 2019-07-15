import pandas as pd

# Read the data
file_loc = input("Enter the path of your csv file: ")
df = pd.read_csv(file_loc)
pred_variable = input("Enter the name of prediction variable: ")

# Find cateogrical columns that need to be encoded
cat_cols = df.select_dtypes(exclude=['int', 'float']).columns
cat_cols = set(cat_cols) - {pred_variable}
cat_cols = list(cat_cols)

# Iterate over the columns to encode them
for a in range(0, len(cat_cols)):
    one_hot_temp = pd.get_dummies(df[cat_cols[a]])
    if(one_hot_temp.shape[1] > 200):
        raise SystemExit('Error: Column ' + cat_cols[a] +
                         'has more than 200 categories.' +
                         ' Exiting as the feature size' +
                         ' is too big.')
    df = df.drop(cat_cols[a], axis=1)
    df = df.join(one_hot_temp)

# Write this dataframe to a csv
write_loc = file_loc[0:-4] + '_one_hot_encoded.csv'
df.to_csv(write_loc, index=False)
