"""
Offers various summations of crime data from Portland, Oregon during the years 2011-2014
Gives user options for the most and least of any option, like zip code or year

"""
from collections import Counter
import os


CRIME_DIR = '/home/roger/Git/PythonFullStack/1_Python/3_Applied_Python/labs/pdx_crime_data/data/'



def opener(path):
    """
    opens the appropriate file determined by user input
    """
     with open(CRIME_DIR+path, 'r') as file:
         text = file.read()
         return text


def splitter(text):
    """
    splits data from a string to a list
    :param text: text from opener function
    :return: data that has been split according to each row
    """
    records = text.split()
    splitted = {}

    for record in records:
        splitted[record] = splitted.get(record, 0) + 1
    return splitted

def sorter(splitted):
    """

    :param splitted: sorts data from splitter function by crime
    :return: sorted data
    """
    sort_done = splitted.sort(key=[3])
    return sort_done

def counter(dataset) :
    """
    :param dataset: counts the number of crimes per category
    :return: list of crimes
    """
    crimes = [crime[3] for crime in dataset]
    c = Counter


def filter(dataset, query):
    """
    counts the number of instances of each category
    :return: list of each crime
    """
    result = len([crime for crime in dataset if query in crime])
    return result

def maximizer():
    """

    :return: the category and number of the most number of crimes
    """
    result = len([crime for crime in dataset if query in crime])
    maximized = max(result)

def minimizer():
    """
    :return: the category and number of the least number of crimes
    """
    result = len([crime for crime in dataset if query in crime])
    minimized = min(result)

def menu():
    """
    requests user input

    """
    options = {choice: filename for choice, filename in enumerate(os.listdir(CRIME_DIR), start=1)}
    for choice, filename in options.items():
        print(options)

    user_input = input()

def o2rta():
    """
    One to Rule Them All
    :return: the maximum and minimum number of crimes and the name of the crimes
    """
    menu()
    opener(user_input)
    splitter()
    sorter()
    counter()
