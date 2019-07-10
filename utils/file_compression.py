import glob
import zlib
import zipfile
import os

def compress_files(regex="age_project*", out_file="age_project.zip"):
     """
          Zips files matching a regex
          Args:
               regex (str): pattern you want to match to filter out files
               out_file (str): The name of the zip file you want to generate.
          Returns: N/A
     """
     files = glob.glob(regex)  # get all files you want to zip

     # Select the compression mode ZIP_DEFLATED for compression
     # or zipfile.ZIP_STORED to just store the file
     compression = zipfile.ZIP_DEFLATED
     # create the zip file first parameter path/name, second mode
     zf = zipfile.ZipFile(out_file, mode="w") 

     try:
          for file_name in files:
               # Add file to the zip file
               # first parameter file to zip, second filename in zip
               zf.write(file_name, file_name, compress_type=compression)
               os.remove(file_name) #remove file from data/ directory because already added to zipfile
     except FileNotFoundError:
          print("An error occurred")
     finally:
          zf.close() # Don't forget to close the file!

     print(out_file + " has been zipped") # let user know file has been zipped


if __name__ == "__main__":

     #compressing age files
     compress_files("../Guess_My_Age/data/age_project_3*", "../Guess_My_Age/data/age_project_3.zip")
     compress_files("../Guess_My_Age/data/age_project_4*", "../Guess_My_Age/data/age_project_4.zip")