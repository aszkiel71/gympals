import bmi_calc
import user
import bf_calc
import trainings
import onemaxrep
import calories_calc
import training_plan

def clear():
  print("\n"*120)

def menu_verify_value(expected_values: list, input: any):
    #   Function for checking if user has chosen an existing menu option
    if input in expected_values:
        return True
    else:
        return False


def menu_option(expected_values: list):
    #   Function used for selecting an option
    decision = input("Select an option: ")
    while not menu_verify_value(expected_values, decision):
        decision = input(f"Select a correct option, correct options are: {expected_values}      : ")
    return decision

def exercises():
    with open("exercises.txt", "r") as exercises_file:
        body_parts = set()
        exercises = {}
        lines = [line.strip().split() for line in exercises_file.readlines()]
        for line in lines:
            body_parts.add(line[0])
        (list(body_parts)).sort()
        for body_part in body_parts:
            exercises[body_part] = []
        for line in lines:
            exercises[line[0]].append(line[1])
        return exercises

def login_screen():
    #   True - user logged; False - unsuccessful logging, exit program
    print("Welcome to GymPals!")
    print("1. Login to an existing account")
    print("2. Make a new account")
    decision = menu_option(["1", "2"])

    if decision == "1":
        print("You are logging in.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if not current_user.login(username, password):
            print("Logging was unsuccessful")
            return False
        else:
            print(f"Welcome to GymPals {current_user.username}!")
            return True
    elif decision == "2":
        print("You are making a new account at GymPals!")
        username = input("Enter your login: ")
        password = input("Enter your password: ")
        email = input("Enter your e-mail: ")
        if not current_user.register(username, password, email):
            print("Registering was unsuccessful")
            return False
        else:
            print("You have successfully created an account!")
            return True


def main_menu():
    print("==========GYMPALS==========")
    print("1. Enter a new training\n2. Past trainings\n3. Calculators\n4. User settings\n5. Workout plan\n6. Exit GymPals")
    decision = menu_option(["1", "2", "3", "4", "5", "6"])
    if decision == "1":
        trainings.new_training(current_user.user_id)
        main_menu()
    elif decision == "2":
        trainings.view_trainings(str(current_user.user_id))
        main_menu()
    elif decision == "3":
        print("==========CALCULATORS==========")
        print("1. BMI calculator\n2. Body fat calculator\n3. One max rep calculator\n4. Requirement calories calculator")
        decision = menu_option(["1", "2", "3", "4"])
        if decision == "1":
            bmi_calc.bmi_calculator(current_user)
        elif decision == "2":
            bf_calc.app(current_user)
        elif decision == "3":
            onemaxrep.app()
        elif decision == "4":
            calories_calc.app(current_user)

        main_menu()
    elif decision == "4":
        print("==========USER SETTINGS==========")
        print("1. Change account settings.\n2. Change or add body data")
        decision = menu_option(["1", "2"])
        if decision == "1":
            current_user.change_settings()
        elif decision == "2":
            current_user.body_data()
        main_menu()
    elif decision == "5":
        training_plan.main(current_user)
        main_menu()
    elif decision == "6":
        exit()


if __name__ == "__main__":
    current_user = user.User()
    if login_screen():
        main_menu()
    else:
        exit()
