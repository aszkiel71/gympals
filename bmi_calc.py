import main
import time


def bmi_calc_end_screen(user):
    print("Do you want to check again for other data?")
    does_he_want = input("Type 'Yes' or 'No' or type '3' if you want to check for your data: ")
    if does_he_want in ("Yes", "yes", "ye", "yup", "'yes'", "'yup'", "'Yes'", "'ye'"):
        bmi_calc_math()
    elif does_he_want in ("No", "no", "nah", "fuck you", "'No'", "'nah'", "'no'", "'fuck you'"):
        print("Returning to the app ...")
        time.sleep(2)
    elif does_he_want in ("3", "three", "third", "'3'", "'three'", "'third'"):
        bmi_calc_users_bmi(user)  # Here come back to enter the data for guest

# Feedback to user
def bmi_calc_cradle(bmi):
    if 0 <= bmi < 18.5:
        print("You are underweight.")
    if 18.5 <= bmi <= 24.99:
        print("Your body weight is normal.")
    if 25 <= bmi <= 29.99:
        print("You are overweight.")
    if 30 <= bmi <= 34.99:
        print("You have first-degree obesity.")
    if 35 <= bmi <= 40:
        print("You have second-degree obesity.")
    if 40 < bmi:
        print("You have third-degree obesity.")

def bmi_calc_users_bmi(user):
    if "None" in [user.weight, user.height]:
        print("Enter body data first!")
        return None
    user_bmi = round(user.weight/(user.height/100)**2, 2)
    print("Your Body Mass Index is: ", user_bmi)
    bmi_calc_cradle(user_bmi)
    bmi_calc_end_screen(user)

def bmi_calc_math():
    temp_weight_of_bmi = float(input("Enter you weight in KG : "))
    temp_height_of_bmi = float(input("Enter your height in CM : "))
    bmi = round(temp_weight_of_bmi/(temp_height_of_bmi/100)**2, 2)
    print("Your Body Mass Index is: ", bmi)
    bmi_calc_cradle(bmi)
    bmi_calc_end_screen(bmi)

def bmi_calculator(user):
    ################################################## INTRODUCTION TO THE CALCULATOR
    print("----- BMI Calculator -----")
    print("Do you want to calculate BMI for: \n 1. your height and weight \n 2. for someone else? ")
    decision_bmi = input("Choose number (1 or 2): ")
    ################################################### MATH
    temp_height_of_bmi = 0 # for guests ( NOT FOR USER )
    temp_weight_of_bmi = 0 # for guests ( NOT FOR USER )
    height_user = 180 # Potem zmienie by pobierało z pliku
    weight_user = 80  # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    if decision_bmi == "1":
        if bmi_calc_users_bmi(user) is None:
            pass
    elif decision_bmi == "2":
        bmi_calc_math()
