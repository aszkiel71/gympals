import main
import user
import time

def app(user):
    print("Would you like to calculate your caloric requirement for you (then type 1) or for someone else (then type 2)?")
    decision = main.menu_option(["1", "2"])
    if decision == '1':
        pass
    if decision == '2':
        print("Enter your sex [male / female]")
        sex = main.menu_option(["1", "male", "man", "MAN", "Man", "2", "female", "woman", "Woman"])
        weight = float(input("Enter your weight : "))
        if sex in ("1", "male", "man", "MAN", "Man"):
            print("You need to remember that the figures given are only approximate")
            print(f"Your basic caloric requirement equal {round(22*weight, 0)}kcal!")
            print("That is, if you sat on a stool all day and did nothing your weight would not change as if you ate as much")
        else:
            print("You need to remember that the figures given are only approximate")
            print(f"Your basic caloric requirement equal {round(22*weight-300, 0)}kcal!")
            print("That is, if you sat on a stool all day and did nothing your weight would not change as if you ate as much")
    print("Now we're going to ask you a couple of questions to include your physical effort during the day in the calculations")
    useless = input("How many days a week do you go to the gym (etc.)? : ")   # it not gonna be use in any formula xD
    print("What is your lifestyle? Type 1 if sedentary, 2 if moderately active, 3 if active, 4 if very active.")
    active = int(main.menu_option(['1', '2', '3', '4']))
#    tab_active = {1 : 'sedentary', 2 : 'moderately active', 3 : 'active', 4 : 'very active'}   # might be useful in future
    tab_formula = {1 : 1.4, 2 : 1.65, 3 : 1.9, 4: 2.15}
    if decision == '2':
        if sex in ("1", "male", "man", "MAN", "Man"):
            print(f"Your caloric requirement equal {round(22*weight*tab_formula[active], 0)}")
            print("Would you like to check for another data ? yes / no ")
            query = main.menu_option(["yes", "no"])
            if query == "yes":
                app(user)
            if query == "no":
                print("Returning to the app ... ")
                time.sleep(1)
        else:
            print(f"Your caloric requirement equal {round(22*weight*tab_formula[active]-400, 0)}")
            print("Would you like to check for another data ? yes / no ")
            query2 = main.menu_option(["yes", "no"])
            if query2 == "yes":
                app(user)
            if query2 == "no":
                print("Returning to the app ... ")
                time.sleep(1)
    if decision == '1':
        if user.sex == 'male':
            print(f"Your basic caloric requirement equal {round(22*user.weight, 0)}kcal!")
            print(f"Your caloric requirement (according to your lifestyle) equal {round(22*user.weight*tab_formula[active], 0)}kcal")
        elif user.sex == 'female':
            print(f"Your basic caloric requirement equal {round((22*user.weight-450), 0)}kcal!")
            print(f"Your caloric requirement (according to your lifestyle) equal {round((22*user.weight*tab_formula[active]-400), 0)}kcal")
        elif user.sex == "none" or "NONE" or "None":
            print("To continue make sure you have the required data (such as gender and weight)")


