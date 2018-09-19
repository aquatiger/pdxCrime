"""
Developing tests for PDX crime data
"""

import unittest
from PDXcrime import opener, menu, CRIME_DIR


class TestCrimeData(unittest.TestCase):
    def setUp(self):
        self.test_data = '''
        "Record ID","Report Date","Report Time","Major Offense Type","Address","Neighborhood","Police Precinct","Police District",X Coordinate,Y Coordinate
        "13807517","12/01/2011","01:00:00","Liquor Laws","NE WEIDLER ST and NE 1ST AVE, PORTLAND, OR 97232","LLOYD","PORTLAND PREC NO","690",7647471.0160800004,688344.45013000001
        "13716403","07/07/2011","18:30:00","Liquor Laws","NE SCHUYLER ST and NE 1ST AVE, PORTLAND, OR 97212","ELIOT","PORTLAND PREC NO","590",7647488.1558400001,688869.34843000001
        "13690826","05/27/2011","08:45:00","Liquor Laws","NE HANCOCK ST and NE 1ST AVE, PORTLAND, OR 97212","ELIOT","PORTLAND PREC NO","590",7647496.6292700004,689129.14205999998
        "13684158","05/16/2011","08:40:00","Liquor Laws","NE HANCOCK ST and NE 1ST AVE, PORTLAND, OR 97212","ELIOT","PORTLAND PREC NO","590",7647496.6292700004,689129.14205999998
        "13690824","05/27/2011","08:35:00","Liquor Laws","NE SCHUYLER ST and NE 1ST AVE, PORTLAND, OR 97212","ELIOT","PORTLAND PREC NO","590",7647488.1558400001,688869.34843000001
        "13658976","04/05/2011","02:08:00","Motor Vehicle Theft","NE HANCOCK ST and NE 1ST AVE, PORTLAND, OR 97212","ELIOT","PORTLAND PREC NO","590",7647496.6292700004,689129.14205999998
        "13704097","06/14/2011","03:01:00","Arson","NE HANCOCK ST and NE 1ST AVE, PORTLAND, OR 97212","ELIOT","PORTLAND PREC NO","590",7647496.6292700004,689129.14205999998
        "13631675","02/15/2011","12:25:00","Drugs","NW DAVIS ST and NW 1ST AVE, PORTLAND, OR 97209","CHINA/OLD TOWN","PORTLAND PREC CE","822",7645653.23917,684826.79559999995
        "13658977","04/05/2011","02:34:40","Motor Vehicle Theft","SW HANCOCK ST and NE 1ST AVE, PORTLAND, OR 97212","ELIOT","PORTLAND PREC NO","590",7647496.6292700004,689129.14205999998
        "13704098","06/14/2011","03:01:00","Arson","NW HANCOCK ST and NE 1ST AVE, PORTLAND, OR 97212","ELIOT","PORTLAND PREC NO","590",7647496.6292700004,689129.14205999998
        "13631679","02/15/2011","12:25:00","Drugs","NW DAVIS ST and NW 1ST AVE, PORTLAND, OR 97209","CHINA/OLD TOWN","PORTLAND PREC CE","822",7645653.23917,684826.79559999995
        "13739679","08/12/2011","19:00:00","Larceny","NW DAVIS ST and NW 1ST AVE, PORTLAND, OR 97209","CHINA/OLD TOWN","PORTLAND PREC CE","822",7645653.23917,684826.79559999995
        '''

    def test_opener(self):
        filename = "crime_incident_data_2011.csv"
        raw_data = opener(filename)
        self.assertIsNotNone(raw_data, 'Fetching data from file failed.')
        self.assertIsInstance(raw_data, str, 'File data must be a string')
        self.assertDictContainsSubset(raw_data, drugs, 'Data does not contain subset: Drugs')
        self.assertDictContainsSubset(raw_data, arson, 'Data does not contain subset: Arson')
        self.assertDictContainsSubset(raw_data, 'Liquor Laws', 'Data does not contain subset: Liquor Laws')
        self.assertDictContainsSubset(raw_data, theft, 'Data does not contain subset: Theft')
        self.assertDictContainsSubset(raw_data, larceny, 'Data does not contain subset: Larceny')
        self.assertNotIsInstance(raw_data, list, 'Data is list')
        self.assertNotIsInstance(raw_data. dict, 'Data is dictionary')
        self.assertNotIsInstance(raw_data, tuple, 'Data is a tuple')

    def test_splitter(self):
        split_data = splitter(self.test_data)
        self.assertIsNotNone(split_data, 'Data is None')
        self.assertIsInstance(split_data, list, 'Data is not a list')
        self.assertNotIsInstance(raw_data. dict, 'Data is dictionary')
        self.assertNotIsInstance(raw_data, tuple, 'Data is a tuple')
        self.assertEquals(len(split_data), 13)
        self.assertIsInstance(split_data[0], list, 'First element is not a list')

    def test_sorter(self):
        split_data = splitter(self.test_data)
        sorted_data = split_data
        self.assertEquals(len(sorted_data), 13, 'Data is not equal')
        self.assertIsInstance(sorted_data, list, 'Data is not a list')
        self.assertNotIsInstance(raw_data. dict, 'Data is dictionary')
        self.assertNotIsInstance(raw_data, tuple, 'Data is a tuple')

    def test_counter(self):
        self.assertEquals(len(crimes), 13, 'Data length is not equal to beginning length')
        self.assertIsInstance(self.test_data, list, 'Data is not a list')
        self.assertNotIsInstance(raw_data. dict, 'Data is dictionary')
        self.assertNotIsInstance(raw_data, tuple, 'Data is a tuple')
        self.assertIsNotNone(self.test_data, 'Data is None')


    def test_filter(self):
        split_data = splitter(self.test_data)
        filtered = filtered(split_data)
        self.assertIsNotNone(filtered, 'Data is None')
        self.assertEquals(len(filtered), 12, 'Data is not the correct amount of crimes')
        self.assertIsInstance(filtered, dict, 'Data is not a dictionary')
        self.assertNotIsInstance(raw_data. list, 'Data is list')
        self.assertNotIsInstance(raw_data, tuple, 'Data is a tuple')

    def test_maximizer(self):
        maximized = maximizer(self.test_data)
        self.assertIsNotNone(maximized, 'Data is None')
        self.assertIsInstance(maximized, list, 'Data is not a list')
        self.assertNotIsInstance(maximized.dict, 'Data is dictionary')
        self.assertNotIsInstance(maximized, tuple, 'Data is a tuple')
	self.assertRaises(ValueError, 'Data has a ValueError')

    def test_minimizer(self):
        minimized = minimizer(self.test_data)
        self.assertIsNotNone(minimized, 'Data is None')
        self.assertIsInstance(minimized, list, 'Data is not a list')
        self.assertNotIsInstance(minimized.dict, 'Data is dictionary')
        self.assertNotIsInstance(minimized, tuple, 'Data is a tuple')
	self.assertRaises(ValueError, 'Data has a ValueError)

    def test_menu(self):
        self.assertIsNotNone(self.test_data, dict, 'Data is None')
        self.assertIn("crime_incident_data_2011.csv",
                       '/home/roger/Git/PythonFullStack/1_Python/3_Applied_Python/labs/pdx_crime_data/data/',' \
                       'File is not in directory')
        self.assertIn("crime_incident_data_2012.csv",
                      '/home/roger/Git/PythonFullStack/1_Python/3_Applied_Python/labs/pdx_crime_data/data/', ' \
                      'File is not in directory')
        self.assertIn("crime_incident_data_2013.csv",
                      '/home/roger/Git/PythonFullStack/1_Python/3_Applied_Python/labs/pdx_crime_data/data/', ' \
                      'File is not in directory')
        self.assertIn("crime_incident_data_2014.csv",
                      '/home/roger/Git/PythonFullStack/1_Python/3_Applied_Python/labs/pdx_crime_data/data/', ' \
                      'File is not in directory')

