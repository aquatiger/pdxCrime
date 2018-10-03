import csv
from collections import Counter

# use pandas, pandas.read_csv(skipinitialspace, nrows=)
# nrows is good for using only a part of the dataset

CRIME_DIR = 'C:/Users/Roger/Documents/GitHub/pdxCrime/data/crime_incident_data_'

def opener(crimeYear):
    with open(CRIME_DIR+ crimeYear+'.csv', 'r') as file:
       opened = csv.DictReader(file)
       headering = []
####       commonest = Counter(opened['Neighborhood']).most_common(1)
##       print(commonest)
       for row in opened:
           headering.append(row)
           print(headering)
#    file.close()

opener('2014')
