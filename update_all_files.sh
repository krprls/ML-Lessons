#!/bin/bash

#Guess_My_Age data generation and compression
python3 Guess_My_Age/data_generation_age.py Guess_My_Age/data/
python3 utils/file_compression.py Guess_My_Age/data/ age_project_3* age_project_3.zip
python3 utils/file_compression.py Guess_My_Age/data/ age_project_4* age_project_4.zip

#Guess_My_Mood data generation and compression
python3 Guess_My_Mood/data_generation_mood.py Guess_My_Mood/data/
python3 utils/file_compression.py Guess_My_Mood/data/ mood_project_4* mood_project_4.zip

#Averages data generation and compression
python3 Averages/data_generation_averages.py Averages/data/
python3 utils/file_compression.py Averages/data/ averages_project_4* averages_project_4.zip

#Sorting_hat data generation and compression
python3 Sorting_hat/data_generation_sorting_hat.py Sorting_Hat/data/
python3 utils/file_compression.py Sorting_Hat/data/ sortinghat_project_3* sortinghat_project_3.zip
