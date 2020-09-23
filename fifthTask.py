import requests
import json
import csv
import xml.etree.ElementTree as ET

def issetInArray(array, value):
	for i in array: 
		if (i == value):
			return True
	return False

url = 'http://www.cbr.ru/scripts/XML_dynamic.asp'
date = dict(date_req1="01/03/2020", date_req2="01/07/2020")
dollar = dict(VAL_NM_RQ = "R01235")
euro = dict(VAL_NM_RQ = "R01239")
rupia = dict(VAL_NM_RQ = "R01270")
grivna = dict(VAL_NM_RQ = "R01720")
valuts = (dollar, euro, rupia, grivna)

course = dict();

for valuta in valuts:
  query = dict(list(date.items()) + list(valuta.items()))
  request = requests.get(url, query).text
  tree = ET.fromstring(request)
  for child in tree:
    if (not issetInArray(course, child.attrib["Date"])):
      course[child.attrib["Date"]]=[]
    course[child.attrib["Date"]].append(child[1].text)


outputFile = open("outputData/outputStatistic.csv", 'w')

output = csv.writer(outputFile)
output.writerow(["date", "Dollar USA", "Euro", "Rupia", "Grivna"])

for valuePerDate in course:
  output.writerow([valuePerDate, course[valuePerDate]])
outputFile.close()
