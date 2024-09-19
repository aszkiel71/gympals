# PLANY TRENINGOWE
import time
import main
import user
import bmi_calc
#import plany # ! YET DOES NOT EXIST !
def main(user):   #   nazwy funkcji normalne
    print("Hi! Before you receive plan from us, we need to ask you about few things to prepare well training plan especially for you!")
    experience = int(input("type 1 if beginner, 2 if novice, 3 if intermediate or 4 if advanced (or 5 if you are CBUM :) ) "))                        # experience

    if experience not in range(0, 6):
        print("You have entered a wrong data ! You need to start again \n\n\n")
        time.sleep(1)
        main()
    if experience == 5:
        print("Contact us via email: nigga@czarnuchy.org\n\n\n")
        time.sleep(1.5)
        main(user)

    availability = int(input("How many days a week can you devote to workout? [1 - 7] : "))            # availability
    if availability not in range(1, 8):
        print("You have entered a wrong data ! You need to start again \n\n\n")
        time.sleep(1)
        main()
    matching_plan(user, experience, availability)

def matching_plan(user, experience, availability):


############## PLANY TRENINGOWE DLA MEZCZYZN
    plan_for_men_exp_1 = {1: "Plan A 1", 2: "Plan B 1 ", 3: "Plan C 1", 4: "Plan D 1"}            # PEWNIE SIE ZASTANAWIASZ NA CHUJ TU TYLE SLOWNIKOW
    plan_for_men_exp_2 = {1: "Plan A 2", 2: "Plan B 2", 3: "Plan C 2", 4: "Plan D 2"}             # OTÓZ KURWA KAZDY PLAN np PLAN A 2 jest inny OD np PLAN A 1
    plan_for_men_exp_3 = {1: "Plan A 3", 2: "Plan B 3", 3: "Plan C 3", 4: "Plan D 3"}             # I CHUJ
    plan_for_men_exp_4 = {1: "Plan A 4", 2: "Plan B 4", 3: "Plan C 4", 4: "Plan D 4"}             # W DALSZEJ WERSJI BEDZIE PRZEKIEROWANIE DO DRUGIEGO PROGRAMU PYTHON'A
    plan = {1: "niger"}                                                                           # I MOZLIWE ZE TEN KOD Z DOBIERANIEM TEZ BEDZIE W TAMTYM PROGRAMIE ALE NA RAZIE
                                                                                                  # JEST TUTAJ
############ PLANY TRENINGOWE DLA K*BIET
    plan_for_women_exp_1 = {1: "Plan A 1", 2: "Plan B 1 ", 3: "Plan C 1", 4: "Plan D 1"}
    plan_for_women_exp_2 = {1: "Plan A 2", 2: "Plan B 2", 3: "Plan C 2", 4: "Plan D 2"}
    plan_for_women_exp_3 = {1: "Plan A 3", 2: "Plan B 3", 3: "Plan C 3", 4: "Plan D 3"}
    plan_for_women_exp_4 = {1: "Plan A 4", 2: "Plan B 4", 3: "Plan C 4", 4: "Plan D 4"}
############ ----------------------------


    if user.sex == 'male':
        if float(experience) == 1:
            if availability < 5:
                print(plan_for_men_exp_1[availability])
            else:
                print("Plan CHUJ1")
        if float(experience) == 2:
            if availability < 5:
                print(plan_for_men_exp_2[availability])
            else:
                print("Plan CHUJ2")
        if float(experience) == 3:
            if availability < 5:
                print(plan_for_men_exp_3[availability])
            else:
                print("Plan CHUJ3")
        if float(experience) == 4:
           if availability < 5:
                print(plan_for_men_exp_4[availability])
           else:
                print("Plan CHUJ4")

          # FOR WOMEN

    if user.sex == 'female':
        if float(experience) == 1:
            if availability < 5:
                print(plan_for_women_exp_1[availability])
            else:
                print("Plan CHUJ1")
        if float(experience) == 2:
            if availability < 5:
                print(plan_for_women_exp_2[availability])
            else:
                print("Plan CHUJ2")
        if float(experience) == 3:
            if availability < 5:
                print(plan_for_women_exp_3[availability])
            else:
                print("Plan CHUJ3")
        if float(experience) == 4:
           if availability < 5:
                print(plan_for_women_exp_4[availability])
           else:
                print("Plan CHUJ4")


#main()
