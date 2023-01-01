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
#Influential for an individual’s medical insurance charges
#Which is the region with the most smokers
#Which is the average cost for each region
#Which is the average age on smokers 

def average_column(column):
    sum = 0
    for i in column:
        sum += float(i)
    total = sum / len(column)
    return total

def create_dictionary(column1, column2):
    dictionary =  {key:value for key, value in zip(column1, column2)}
    return dictionary

age_smokers = create_dictionary(smokers, ages)
    
print(average_column(charges))
    

    



