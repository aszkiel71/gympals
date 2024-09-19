import main
import time
import user
def app():
    print("Hi! Enter the number of repetitions of the pressed weight [range from 2 to 10 inclusive] ")
    reps = int(main.menu_option([str(i) for i in list(range(2, 11))]))
    weight = float(input("Next, give the pressed weight [kilograms] : "))
    calc(reps, weight)

def query():
    print("Would you like to check for another data ?\nType yes or no")
    query = main.menu_option(['yes', 'YES', 'Y', 'y', 'Yes', 'Yup', '1', 'nah', 'Nah', 'No', 'no', 'NO', 'N', 'n', '2'])
    if query in ('yes', 'YES', 'Y', 'y', 'Yes', 'Yup', '1'):
        app()
    elif query in ('1', 'nah', 'Nah', 'No', 'no', 'NO', 'N', 'n', '2'):
        print("\nReturning to the app ... ")
        time.sleep(1)

def calc(reps, weight):
    tab = {2 : 0.935, 3 : 0.91, 4 : 0.885, 5 : 0.86, 6 : 0.84675, 7 : 0.835, 8 : 0.785, 9 : 0.76, 10 : 0.735}
    print(f"Your one max rep : {round(weight/tab[reps], 0)}")
    query()

#app()

