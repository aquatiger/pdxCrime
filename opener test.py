import csv
from collections import Counter
#import numpy as np

# use pandas, pandas.read_csv(skipinitialspace, nrows=)
# nrows is good for using only a part of the dataset

CRIME_DIR = 'C:/Users/Roger/Documents/GitHub/pdxCrime/data/crime_incident_data_'

def opener(crimeYear):
    with open(CRIME_DIR+ crimeYear+'.csv', 'r') as file:
           opened = csv.DictReader(file)
           csvHeadings = next(opened)
           print(csvHeadings)
           for row in opened:
                  print(row)
##       headering = {}
#    with open('crimes.csv', 'w') as newFile:

##           crimes = csv.DictWriter(newFile)
##           fieldnames = crimes.writeheader()
##           print(fieldnames)
##           for row in opened:
##               crimes.writerow('Major Offense Type')
##               print(crimes)
##       for row in opened:
####           if row not in headering:
####               #headering.append(row)
####               opened[row][3] += 1
####               print(row[3])

opener('2014')


####       commonest = Counter(opened['Neighborhood']).most_common(1)
##       print(commonest)
##
##       #this opens the file and reads the first line to use as headings
##           opening = csv.reader(file)
##           csvHeadings = next(opening)
##           print(csvHeadings)

