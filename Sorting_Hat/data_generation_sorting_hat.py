import pandas as pd
import csv
import numpy as np
import sys

def main():
    path = 'data/'
    if (len(sys.argv)) > 1:
        path = sys.argv[1]

    src_file = 'Sorting_Hat_Full_Dataset.csv'
    dataset = pd.read_csv(path + src_file)

    # LESSON 3 --SKEW DATA
    # 1. Only one Gryffindor example
    num_samples = len(dataset)
    g_num_samples = len(dataset.query('house == "Gryffindor"'))
    one_sample_fraction = 1/(num_samples-g_num_samples+1)
    dest_file_name = path + "sortinghat_project_3_one_gryff.csv"
    skew_data(one_sample_fraction, dataset, dest_file_name)

    # 2. 10% Gryffindor samples
    dest_file_name = path + "sortinghat_project_3_10_percent_gryff.csv"
    skew_data(0.1, dataset, dest_file_name)

    # 3. 30% Gryffindor samples
    dest_file_name = path + "sortinghat_project_3_30_percent_gryff.csv"
    skew_data(0.3, dataset, dest_file_name)

    # 4. 50% Gryffindor samples
    dest_file_name = path + "sortinghat_project_3_50_percent_gryff.csv"
    skew_data(0.5, dataset, dest_file_name)

def skew_data(desired_fraction, data, dest_file_name):
    """
    Generate data that contain a certain fraction of Gryffindor samples
    Args:
        fraction (float): Fraction of samples that should be Gryffindor
        data (DataFrame): Original data
    Returns:
    """
    # Calculate the current fraction of Gryffindor samples
    g_num_samples = len(data.query('house == "Gryffindor"'))
    total_samples = len(data)
    g_fraction = g_num_samples/total_samples

    # If the fraction of Gryffindor samples is less than
    # required, drop samples from other houses
    # else, drop samples from Gryffindor
    if(g_fraction < desired_fraction):
        desrired_other_labels_count = int(g_num_samples*(1-desired_fraction)/desired_fraction)
        other_labels_current = total_samples - g_num_samples
        data = data.drop(data.query('house != "Gryffindor"')
                         .sample(n=(other_labels_current-desrired_other_labels_count), random_state=104729).index)
    else:
        desired_g_labels_num = int(np.ceil((total_samples - g_num_samples)*desired_fraction/(1-desired_fraction)))
        data = data.drop(data.query('house == "Gryffindor"')
                         .sample(n=(g_num_samples-desired_g_labels_num), random_state=104729).index)

    # Write data to file
    data.to_csv(dest_file_name, index=False)
    print(dest_file_name + " data saved")


if __name__ == "__main__": 
    main()
