'''These are the variables we will need to create:
   - `age`: age of the individual in years
   - `sex`: 0 for female, 1 for male*
   - `bmi`: individual's body mass index
   - `num_of_children`: number of children the individual has
   - `smoker`: 0 for a non-smoker, 1 for a smoker
   '''

# create the initial variables below
age =28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0


# Add insurance estimate formula below
insurance_cost = 250*age -128 *sex+370*bmi+425*num_of_children+24000*smoker-12500

#print result
print( "This person's insurance cost is " + str(insurance_cost) + " dollars.")

# add 4 years to age
age += 4

# Add new insurance estimate formula below
new_insurance_cost = 250*age -128 *sex+370*bmi+425*num_of_children+24000*smoker-12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# rewrite age as original age
age = 28

# add 3.1 to bmi
bmi += 3.1

# calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# calculate change between the new insurance cost and original insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")


# rewrite bmi as original value
bmi = 26.2

# male vs. female factor
# change value of sex to 1
sex = 1

# calculate the new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# calculate change between the new insurance cost and original insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")