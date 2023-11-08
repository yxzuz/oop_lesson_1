#---------------------PYTHON VERSION--------------------------
#
# import csv,os
# # for finding CSV directory????
# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))
#
#
# # Read and Store Data from 'Cities.csv':
# cities = []  # store cities data from CSV files
# # opens the 'Cities.csv' file located in the directory
# with open(os.path.join(__location__, 'Cities.csv')) as f:
#     rows = csv.DictReader(f) # opens the 'Cities.csv' file located in the directory
#     for r in rows:
#         cities.append(dict(r))
#
# countries = []  # store countries data from CSV files
# with open(os.path.join(__location__, 'Countries.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         countries.append(dict(r))
#
# # SO RN WE WOULD HAVE 2 LISTS OF DICT
#
# # Print the average temperature for all the cities in Italy
# temps = []
# my_country = 'Italy'
# for city in cities:
#     if city['country'] == my_country:
#         temps.append(float(city['temperature']))
# # print('temp:',temps)
# print(sum(temps)/len(temps))
#
# print()
# # Print all cities that are not in the EU and whose average temperatures are below 5.0
# # Requires joining cities and countries
# import copy
# cities_ext = []  # contains merged list with country and cities
# for city in cities:
#     for country in countries:
#         # Country(key) will overlap so...
#         if city['country'] == country['country']:
#             dict1 = copy.deepcopy(city)
#             dict2 = copy.deepcopy(country)
#             dict1.update(dict2)  # merge two list of dicts with country
#             cities_ext.append(dict1)
# for city in cities_ext:
#     if city['EU'] == 'no' and float(city['temperature']) < 5.0:
#         print(city)

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Read and Store Data from 'Cities.csv':
cities = []  # store cities data from CSV files
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)  # opens the 'Cities.csv' file located in the directory
    # dict reader use for reading the data from these files and store it in lists, cities and countries, as dictionaries.
    for r in rows:
        cities.append(dict(r))

countries = []  # store countries data from CSV files
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# SO RN WE WOULD HAVE 2 LISTS OF DICT

class DB:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)  # add table to database

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None


import copy


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        # create new instance to Class Table with default value empty list
        filtered_table = Table(self.table_name + '_filtered', []) # initialize
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return function(temps) # like sum(x) min(x) max(x)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]  # add key and its value to dict_temp
            temps.append(dict_temp)
        return temps

    def __str__(self):
        return self.table_name + ':' + str(self.table)


table1 = Table('cities', cities)
table2 = Table('countries', countries)
# Class Table has 2 instances: table1, table2
my_DB = DB()  # make instance for class DB
my_DB.insert(table1)
my_DB.insert(table2)
# RN my_DB (Class DB) = [{dict of cities},{dict of countries}]
my_table1 = my_DB.search('cities')

#print(table1 is my_table1)
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
my_table1_selected = my_table1.select(['city', 'latitude'])
print(144,my_table1)
print()
print('my_table1_selected:',my_table1_selected)

print('my_table1_filtered:',my_table1_filtered)
temps = []
for item in my_table1_filtered.table:  # loop for key in table wiht country key: 'italy'
    temps.append(float(item['temperature']))
print(sum(temps) / len(temps)) #avg temp
print("Using aggregation")
# RN WE USE IT FOR AVG
print(my_table1_filtered.aggregate(lambda x: sum(x) / len(x), 'temperature'))

print()
my_table2 = my_DB.search('countries')
my_table3 = my_table1.join(my_table2, 'country')
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print('my_table2',my_table2)
print(my_table3_filtered.table)
print(164,my_table3)

print()
print('Print the min and max temp for cities in EU that have no coastlines')
my_table3EU = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print('filtered table: ',my_table3EU)
print('Max temp:',my_table3EU.aggregate(lambda x: max(x), 'temperature'))
print('Min temp:',my_table3EU.aggregate(lambda x: min(x), 'temperature'))
print()

print('Min latitude', my_table3.aggregate(lambda x: min(x), 'latitude'))
print('Max latitude', my_table3.aggregate(lambda x: max(x), 'latitude'))

