import pandas as pd
import csv


dataset1 = []
dataset2 = []

with open("Pro129/convertedData.csv" , "r") as f :
    for i in csv.reader(f):
        dataset1.append(i)

with open("Pro129/brightStars.csv" , "r") as f :
    for i in csv.reader(f):
        dataset2.append(i)


header1 = dataset1[0]
header2 = dataset2[0]

headers = header1 + header2

planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

planet_data = []

for i in planet_data1:
    planet_data.append(i)

for j in planet_data2:
    planet_data.append(j)

with open("Pro129/FinalData.csv", "a+") as f:
    data = csv.writer(f)
    data.writerow(headers)
    data.writerows(planet_data)









