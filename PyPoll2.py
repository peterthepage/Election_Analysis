import csv
import os

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
#Write some data to the file.
    txt_file.write("Counties in the Election\n-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    