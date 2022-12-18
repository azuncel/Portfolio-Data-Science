# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    analyze_smoker(smoker)
    analyze_bmi(bmi)
    return estimated_cost

def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")


def analyze_bmi(bmi_value):
    if bmi_value > 30:
        print("Obese")
    elif bmi_value >= 25 and bmi_value <= 30:
        print(" overweight")
    elif bmi_value >= 18.5 and bmi_value < 25:
        print("normal weight")
    elif bmi_value < 18.5:
        print("underweight")
   


# Estimate Azu's insurance cost
Azu_insurance_cost = estimate_insurance_cost(name = 'Azu', age = 33, sex = 0, bmi = 26.2, num_of_children = 1, smoker = 1)
print(Azu_insurance_cost)



    