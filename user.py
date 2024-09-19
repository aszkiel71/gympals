import main


class User:

    def __init__(self):
        self.user_id = None
        self.username = None
        self.password = None
        self.email = None
        self.sex = None
        self.age = None
        self.weight = None
        self.height = None
        self.waist_girth = None

    def strike(self, count: int):
        #   Function checking whether to cancel logging/registering or not
        if count > 3:
            return True
        else:
            return False

    def register(self, username: str, password: str, email: str):
        #   False - unsuccessful register; True - successful register
        with open("users", "r+") as user_file:
            strikes = 0
            users = [user.split() for user in user_file.readlines()]
            print(users)
            for user in users:
                while username == user[1]:
                    print("Username is already taken!")
                    strikes += 1
                    if self.strike(strikes):
                        return False
                    username = input("Choose a different username: ")
                while email == user[3]:
                    print("E-mail is already taken!")
                    strikes += 1
                    if self.strike(strikes):
                        return False
                    email = input("Choose a different e-mail or log into existing account: ")

            while len(password) < 6:
                print("Your password is too short! Make a longer password")
                strikes += 1
                if self.strike(strikes):
                    return False
                password = input("Enter new password: ")

            self.username = username
            self.password = password
            self.email = email
            #   Incrementing the last existing user_id by 1
            if len(users) > 0:
                self.user_id = int(users[-1][0]) + 1
            #   First user case
            else:
                self.user_id = 1


            user_file.write(f"{self.user_id} {self.username} {self.password} {self.email} "
                            f"{self.sex} {self.age} {self.weight} {self.height} {self.waist_girth}\n")

            #   self.update_account_data()

            return True

    def find_user(self, username: str):
        #   Function checking if user with such username exists
        with open("users", "r+") as user_file:
            users = [user.split() for user in user_file.readlines()]
            for user in users:
                if user[1] == username:
                    return user
        return False

    def login(self, username: str, password: str):
        #   False - unsuccessful login; True - successful login
        strikes = 0
        while not self.find_user(username):
            print("User does not exist!")
            strikes += 1
            if self.strike(strikes):
                return False
            username = input("Enter your username again: ")

        user = self.find_user(username)
        while password != user[2]:
            print("Password is incorrect!")
            strikes += 1
            if self.strike(strikes):
                return False
            password = input("Enter your password again: ")

        self.user_id = user[0]
        self.username = user[1]
        self.password = user[2]
        self.email = user[3]
        self.sex = user[4]
        self.age = user[5]
        self.weight = user[6]
        self.height = user[7]
        self.waist_girth = user[8]


        return True

    def change_username(self):
        username = input("Enter a new username: ")
        with open("users", "r+") as user_file:
            users = [user.split() for user in user_file.readlines()]
            for user in users:
                while username == user[1]:
                    print("Username is already taken!")
                    username = input("Choose a different username: ")
        self.username = username

    def change_password(self):
        password = input("Enter a new password: ")
        while len(password) < 6:
            print("Your password is too short! Make a longer password")
            password = input("Enter new password: ")
        self.password = password

    def change_email(self):
        email = input("Enter a new e-mail")
        with open("users", "r+") as user_file:
            users = [user.split() for user in user_file.readlines()]
            for user in users:
                while email == user[3]:
                    print("E-mail is already taken!")
                    email = input("Choose a different e-mail: ")
        self.email = email

    def update_account_data(self):
        with open("users", "r") as user_file:
            user_line_number = int(self.user_id) - 1
            lines = user_file.readlines()
            lines[user_line_number] = f"{self.user_id} {self.username} {self.password} {self.email} " \
                                      f"{self.sex} {self.age} {self.weight} {self.height} {self.waist_girth}\n"
        with open("users", "w") as user_file:
            user_file.writelines(lines)
        if "None" not in [self.age, self.weight, self.height, self.waist_girth] \
                and None not in [self.age, self.weight, self.height, self.waist_girth]:
            self.age = int(self.age)
            self.weight = float(self.weight)
            self.height = float(self.height)
            self.waist_girth = float(self.waist_girth)

    def change_settings(self):
        print("==========CHANGE ACCOUNT SETTINGS==========")
        print("1. Change username\n2. Change password\n3. Change e-mail\n4. Delete account\n5. Return to main menu")
        decision = main.menu_option(["1", "2", "3", "4", "5"])

        if decision == "1":
            self.change_username()
            self.update_account_data()
            self.change_settings()
        elif decision == "2":
            self.change_password()
            self.update_account_data()
            self.change_settings()
        elif decision == "3":
            self.change_email()
            self.update_account_data()
            self.change_settings()
        elif decision == "4":
            self.change_settings()
        elif decision == "5":
            pass

    def body_data(self):
        print("==========ADD OR CHANGE BODY DATA==========")

        self.update_account_data()

        status = {"sex": "Add" if self.sex != "None" else "Change",
                  "age": "Add" if self.age != "None" else "Change",
                  "weight": "Add" if self.weight != "None" else "Change",
                  "height": "Add" if self.height != "None" else "Change",
                  "waist_girth": "Add" if self.waist_girth != "None" else "Change"}

        print(f"1. {status['sex']} sex  (Current sex: {self.sex})\n"
              f"2. {status['age']} age   (Current age: {self.age}{' years' if self.age != 'None' else ''})\n"
              f"3. {status['weight']} body mass   (Current weight: {self.weight}{' kg' if self.weight != 'None' else ''})\n"
              f"4. {status['height']} height    (Current height: {self.height}{' cm' if self.height != 'None' else ''})\n"
              f"5. {status['waist_girth']} waist girth   (Current waist girth: {self.waist_girth}{' cm' if self.waist_girth != 'None' else ''})\n"
              f"6. Return to main menu")
        decision = main.menu_option(["1", "2", "3", "4", "5", "6"])

        if decision == "1":
            sex = input("Enter your sex, write either male or female: ").lower()
            while not main.menu_verify_value(["male", "female"], sex):
                sex = input("Enter your sex, PLEASE WRITE either male or female: ").lower()
            self.sex = sex
            self.update_account_data()
            self.body_data()
        elif decision == "2":
            age = input("Enter your age in years: ")
            while not age.isnumeric():
                age = input("Enter your age in years, your age should be between 1 and 99: ")
            self.age = int(age)
            self.update_account_data()
            self.body_data()
        elif decision == "3":
            weight = input("Enter your weight in kilograms: ")
            while not weight.replace(".", "").isnumeric():
                weight = input("Enter your weight in kilograms; please, enter a number: ")
            self.weight = float(weight)
            self.update_account_data()
            self.body_data()
        elif decision == "4":
            height = input("Enter your height in centimeters: ")
            while not height.replace(".", "").isnumeric():
                height = input("Enter your height in centimeters; please, enter a number: ")
            self.height = float(height)
            self.update_account_data()
            self.body_data()
        elif decision == "5":
            waist_girth = input("Enter your waist girth in centimeters: ")
            while not waist_girth.replace(".", "").isnumeric():
                waist_girth = input("Enter your waist girth in centimeters; please, enter a number: ")
            self.waist_girth = float(waist_girth)
            self.update_account_data()
            self.body_data()
        elif decision == "6":
            pass
