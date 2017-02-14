#This code focuses on parsing the code from CSV to JSON objects

import json
import csv

#Steps for the parser
#open CSV file
#Scan through characters

#open csv file as read in
csvInput = open("tmp.csv", "r")
#open json output file as write only
jsonOutput = open("tmp.json", "w")
#column titles to pull information in with
columnNames = ("Document Title", "Saved File Name", "Tags")
#open CSV parser with the input file, searcing the columnNames, and 
#configure it for the excel CSV format
csvReader = csv.DictReader(csvInput, columnNames, dialect = "excel")

#for each row, convert column data into json object and write to file
for row in reader:
	json.dump(row, jsonOutput)
	jsonOutput.write("\n")
