import csv

#Variables
ages =[]
gender=[]
bmis =[]
children=[]
smokers= []
regions = []
charges = []

#Inspect database
with open('python-portfolio-project-starter-files\insurance.csv', 'r') as insurance_csv:
    file = csv.DictReader(insurance_csv)
    for row in file:
        #print(row)
        ages.append(row['age'])
        gender.append(row['sex'])
        bmis.append(row['bmi'])
        children.append(row['children'])
        smokers.append(row['smoker'])
        regions.append(row['region'])
        charges.append(row['charges'])



#Define goals:
#Which is the average of bmi
#Which is the average cost 
#Which is the average age 

def average_column(column):
    sum = 0
    for i in column:
        sum += float(i)
    total = sum / len(column)
    return total

def create_dictionary(column1, column2,title1, title2):
    dictionary_list={}
    num_column = len(column1)
    for i in range(num_column):
        dictionary_list[i] = {title1: column1[i], title2: column2[i]}
    return dictionary_list


print(round(average_column(ages),2))
print(round(average_column(bmis),2))
print(round(average_column(charges),2))
    

    



