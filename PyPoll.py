import os
import csv
file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:
    
    file_to_save=os.path.join("analysis","election_analysis.txt")
#outfile = open (file_to_save, "w")
#outfile.write("Hello World!")
#outfile.close()
   

with open (file_to_load) as election_data:
    #election_data.write("hello  World   2\n")
    #election_data.write("hello\nWorld\n2")
    file_reader= csv.reader(election_data)
    headers=next(file_reader)
    print(headers)
    #for row in file_reader:
     #   print(row)