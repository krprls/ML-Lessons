#!/bin/bash

#Guess_My_Age data generation and compression
python3 Guess_My_Age/data_generation_age.py Guess_My_Age/data/
python3 utils/file_compression.py Guess_My_Age/data/ age_project_3* age_project_3.zip
python3 utils/file_compression.py Guess_My_Age/data/ age_project_4* age_project_4.zip

#Guess_My_Mood data generation and compression
python3 Guess_My_Mood/data_generation_mood.py Guess_My_Mood/data/
python3 utils/file_compression.py Guess_My_Mood/data/ mood_project_4* mood_project_4.zip