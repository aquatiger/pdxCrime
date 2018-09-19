def opener(crimeYear):
    with open('C:/Users/Roger/Documents/GitHub/pdxCrime/data/crime_incident_data_'+ crimeYear+'.csv', 'r') as file:
        text = file.read()
        print('This works')
        return text

opener('2011')
