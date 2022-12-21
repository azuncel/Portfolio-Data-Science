import pandas as pd
import csv

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []


with open('insurance.csv') as csv_info:
    print("hola")

# def load_list(lst, csv_file, column_name):
#     with open(csv_file) as csv_info:
#         csv_dict = csv.DictReader(csv_info)
#         for row in csv_dict:
#             lst.append(row[column_name])
#         return lst

# # look at the data in insurance_csv_dict
# load_list(age, 'insurance.csv', 'age')
# load_list(sex, 'insurance.csv', 'sex')
# load_list(bmi, 'insurance.csv', 'bmi')
# load_list(children, 'insurance.csv', 'children')
# load_list(smoker, 'insurance.csv', 'smoker')
# load_list(region, 'insurance.csv', 'region')
# load_list(charges, 'insurance.csv', 'charges')
