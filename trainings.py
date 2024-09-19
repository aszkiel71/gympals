import main
import datetime


class Training:

    def __init__(self, length):
        self.length = int(length) if length.isnumeric() and int(length) > 0 else None
        self.date = self.add_date()
        self.exercises = []
        self.exercise_details = {}  # sets, reps, kgs

    def save_training(self, id):
        with open("trainings", "a") as file:
            file.write(f"{id} {self.length} {self.date} {self.exercise_details}\n")

    def add_exercises(self):
        print("==========ADD EXERCISES TO YOUR TRAINING==========")
        exercises = main.exercises()
        body_parts = sorted(list(exercises.keys()))
        exercises_count = 1
        while True:
            print(f"==========EXERCISE {exercises_count}==========")
            for nr, body_part in enumerate(body_parts): print(f"{nr + 1}. {body_part.capitalize()}")
            print(f"{len(body_parts) + 1}. Save training")
            decision = main.menu_option([str(i) for i in range(1, len(body_parts) + 2)])
            if decision == str(len(body_parts) + 1):
                print("Your training is saved")
                break
            else:
                body_part_list = int(decision) - 1   # przypisanie indexu wybranej partii, de facto wybranie partii
                body_part = body_parts[body_part_list]  # index - > nazwa czesci ciala
                body_part_exercises = exercises[body_part]   # lista cwiczen dostpenych dla body_part_list (dla danej czesci ciala)

                for nr, exercise in enumerate(body_part_exercises): print(f"{nr + 1}. {exercise.replace('_', ' ')}")
                decision = int(main.menu_option([str(i) for i in range(1, len(body_part_exercises) + 1)])) - 1


                if body_part_exercises[decision] in self.exercises:
                    print("This exercise is already in your training! Choose a different exercise!")
                    continue

                system_weight = input("Do you prefer use kg or lbs? (Type kg or lbs) : ")
                sets = input("Enter the number of sets you did: ")   # serie
                reps = input("Enter the number of reps you did: ")   # reps
                kg = input("Enter the weight you used in sets (just amount): ")    # kgs

                self.exercises.append(body_part_exercises[decision])
                self.exercise_details[body_part_exercises[decision]] = { 'sets': sets, 'reps': reps, 'kg': kg, 'system_weight' : system_weight}
                exercises_count += 1

    def add_date(self):
        year = datetime.datetime.now().year
        print("Select a month of your training")
        month = int(main.menu_option([str(i) for i in range(1, 13)]))
        print("Select a day of your training")
        day = int(main.menu_option([str(i) for i in range(1, 32)]))  # Wiem, nie bierze pod uwage który miesiąc ale mi sie nie chce teraz
        return f"{day}.{month}.{year}"


def new_training(id):
    print("==========NEW TRAINING==========")
    length = input("Enter your training time (in minutes) or enter 0 if you don't know your training's length: ")
    while not (length.isnumeric() and int(length) >= 0):
        length = input("Enter your training time (in minutes); please, enter a number greater or equal to 0: ")
    training = Training(length)
    training.add_exercises()
    training.save_training(id)


def view_trainings(id):
    with open("trainings", "r") as file:
        trainings = file.readlines()
        user_trainings = [training.split() for training in trainings if training[0] == id] # user_trainings
        for nr_t, training in enumerate(user_trainings):     #
            exercise_details_str = " ".join(training[3:])   # laczenie 'training' od 4 znaku do konca
            exercise_details = eval(exercise_details_str)   # eval(string) -> przeksztalacanie stringa # sam do konca nwm czemu to dziala ale na forum czytalem ze tak powinno byc
            print(f"{nr_t + 1}. Training on {training[2]} that lasted {training[1]} minutes: ") # printuje trening, training[2] -> data, training[3] -> length treningu
         #   act_exercises = [t.replace("_", " ") for t in training[3:]]
            for nr_e, details in exercise_details.items():  # iterowanie exercise i detailsow
                sets = details['sets']
                reps = details['reps']
                kg = details['kg']
                system_weight = details['system_weight']
           #     print(f"Exercise : {act_exercises}")
                print(f"    Exercise: {nr_e.replace('_', ' ')}")
                print(f"    Sets: {sets}, Reps: {reps}, Weigth: {kg}{system_weight}")
