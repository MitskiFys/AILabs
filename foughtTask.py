import csv
import json

jsonFile = open("inputData/inputJson.txt", 'r')
data = json.load(jsonFile)
jsonFile.close()
outputFile = open("outputData/outputCSV.csv", 'w')

output = csv.writer(outputFile)
output.writerow(["item", "country", "year", "sales"])

for row in data:
  item = row["item"]
  countrys = row["sales_by_country"]
  for country, years in countrys.items():
    for year, count in years.items():
      output.writerow([item,
                   country,
                   year,
                   count])
outputFile.close()
