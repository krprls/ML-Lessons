import glob
import zlib
import zipfile
import sys
import os

def compress_files(regex, out_file):
     """
          Zips files matching a regex
          Args:
               regex (str): pattern you want to match to filter out files
               out_file (str): The name of the zip file you want to generate.
          Returns: N/A
     """
     #remove zip file if already exists 
     #if this code snippet does not exist, very slow
     if os.path.exists(out_file):
          os.remove(out_file)

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
     except FileNotFoundError:
          print("An error occurred")
     finally:
          zf.close() # Don't forget to close the file!

     print(out_file + " has been zipped") # let user know file has been zipped


if __name__ == "__main__":
     
     if len(sys.argv) != 4:
          print("Please enter a path to the files, regex, and output zipfile.")
          print("Usage: python3 file_compression.py <path_to_files> <regex> <out_zipfile>")
          exit(1)

     path = sys.argv[1] #path to where files to be compresssed are located
     regex = sys.argv[2] #regex to be matched
     out_zipfile = sys.argv[3] #output zipfile

     compress_files(path + regex, path + out_zipfile)  
     print(out_zipfile + " compressed successfully.")
