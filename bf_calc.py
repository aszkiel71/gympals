import time
import main

def cradle(temp_bf, sex):
    if sex == "male":
        if 2 <= temp_bf < 4:
            print("You have got essential body fat content.")
        if 4 <= temp_bf < 8:
            print("You have got low body fat.")
        if 8 <= temp_bf < 20:
            print("You have got normal body fat.")
        if 20 <= temp_bf < 25:
            print("You have got high body fat.")
        if 25 <= temp_bf:
            print("You have got very high level of body fat.")
    elif sex == "female":
        if 10 <= temp_bf < 12:
            print("You have got essential body fat content.")
        if 12 <= temp_bf < 21:
            print("You have got low body fat.")
        if 21 <= temp_bf < 33:
            print("You have got normal body fat.")
        if 33 <= temp_bf < 39:
            print("You have got high body fat.")
        if 39 <= temp_bf:
            print("You have got very high level of body fat.")

def users_bodyfat(user):
    if "None" in [user.sex, user.weight, user.waist_girth]:
        print("Enter body data first!")
        return None
    bf_user_constant = 98.42 if user.sex == "male" else 76.76
    user_bf = round((((user.waist_girth*4.15)/2.54) - 0.082*user.weight - bf_user_constant) / int(user.weight)*2.2, 2) * 100
    print(f"Your Body Fat is: {user_bf-10}%")
    cradle(user_bf-10, user.sex)
    query()

def guests():
    print('Do you want to check the result for a man or a woman?')
    guests_sex = input("type 1 if you are a man or 2 if you are a woman : ")      #   Zmienić na male/female albo cos podobnego
    if guests_sex in ("Man", "Male", "man", "MAN", '1', "one"):
        guests_sex_nr = 0
        bf_constant = 98.42
    elif guests_sex in ("Woman", "Female", "woman", "WOMAN", '2', "two"):
        bf_constant = 76.76
        guests_sex_nr = 1
    else:
        print("You have entered incorrect data ! ")
        guests()
    temp_guests_weight = float(input("Enter you weight in KG : "))
    temp_the_girth_of_guests_waist = float(input("Enter your waist circumference in CM : "))
    guests_bf = round((((temp_the_girth_of_guests_waist*4.15)/2.54) - 0.082*temp_guests_weight - bf_constant) / temp_guests_weight*2.2, 2) * 100
    print(f"Your Body Fat is: {guests_bf-10}%")
    cradle(guests_bf-10, guests_sex_nr)
    query()

def query():
#    bmi_calc_cradle(bmi)
    print("Do you want to check again for other data?")
    does_he_want = input("Type 1 if 'Yes' or 2 if 'No' or type '3' if you want to check for your data: ")
    if does_he_want in ("Yes", "yes", "ye", "yup", "'yes'", "'yup'", "'Yes'", "'ye'", "1"):
        guests()
    elif does_he_want in ("No", "no", "nah", "fuck you", "'No'", "'nah'", "'no'", "'fuck you'", "2"):
        print("Returning to the app ...")
        time.sleep(2)
        # main_menu() -> MAIN MENU OF GymPals
        pass
    elif does_he_want in ("3", "three", "third", "'3'", "'three'", "'third'"):
        users_bodyfat() # Here come back to enter the data for guest
#    cradle(guests_bf)



def app(user):
    ################################################## INTRODUCTION TO THE CALCULATOR
    print("----- Body Fat Level Calculator -----")
    print("Do you want to calculate Body Fat Level for: \n 1. your parameters \n 2. for someone else? ")
    decision = main.menu_option(["1", "2"])
    if decision == "1":
        users_bodyfat(user)
    elif decision == "2":
        guests()

#app()
# WYKURWIA TU JAKIS ERROR KTOREGO KURWA NIE ROZUMIEM I CHUJ
###     pozmieniac nazwy funkcji bf_calc i bmi_calc
