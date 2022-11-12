# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    gender=input("Enter your gender M/F: ")
    birth_strg=input("Enter your birthday (YYYY-MM-DD): ")
    lbs=int(input("Enter your weight in US pounds: "))
    height=int(input("Enter your height in US inches: "))
    
    years=compute_age(birth_strg)
    kilo=kg_from_lb(lbs)
    centimeter=cm_from_in(height)
    bmi=body_mass_index(lbs, height)
    bmr=basal_metabolic_rate(gender, lbs, height, years)

    print(f"Age: {years}")
    print(f"Weight in kg: {kilo}")
    print(f"Height in cm: {centimeter}")
    print(f"Body Mass Index: {bmi}")
    print(f"Basal Metabolic Rate (kcal/day): {bmr}")
   
    pass


def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthdate.year

    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(lbs):
    kg = lbs * 0.45359237
    return kg 


def cm_from_in(inches):
    cm=inches *2.54
    return cm


def body_mass_index(lbs, height):
    bmi= lbs / (height **2) * 10000
    return bmi


def basal_metabolic_rate(gender, lbs, height, years):
   if gender.upper() == "F":
    bmr = 447.593 + 9.247 * lbs + 3.098 * height - 4.330 * years
    return


main()