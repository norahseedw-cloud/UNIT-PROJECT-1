import time
import os

class Game:
    levels = ["Easy", "Medium", "Hard"]

    def __init__(self):
        self.level = "Easy"
        self.score = 0


    def display_header(self,name_of_game:str, attempts=None):
        print("_"*35)
        print(name_of_game.center(35))
        print("_"*35)
        print(f"Level: {self.level}")
        print(f"Score: {self.score}")
        if attempts is not None:
            print(f"Attempts Left: {attempts}")
            print("-"*35)

    def correct(self):
        self.score += 1
        print("Correct!")
        print(f"Score: {self.score}")

    def incorrect(self, attempts):
        print("Incorrect!")
        print(f"Attempts Left: {attempts}")

    def choose_level(self,easy_level,medium_level,hard_level):
        '''
        This function displays a menu for the user to choose a level
        (Easy, Medium, Hard) and calls the corresponding function.
        ---------------
        easy_level : callable
        Function to execute when the user selects the Easy level.
        medium_level : callable
        Function to execute when the user selects the Medium level.
        hard_level : callable
        Function to execute when the user selects the Hard level.
        '''
        menu_level = '''
Choose mode: 
1- Easy Level
2- Medium Level
3- Hard Level
4- Go back to main menu
'''
        while True:

            user_choice = input(menu_level)

            match user_choice:

                case "1":
                    easy_level()

                case "2":
                    medium_level()

                case "3":
                    hard_level()

                case "4":
                    print("BACK")
                    break

                case _:
                    print("Enter a valid number")

    def get_choice(self, message, valid_choices):

        while True:
            try:
                choice = input(message).strip().lower()

                if choice not in valid_choices:
                    raise Exception(f"Please enter one of these: {', '.join(valid_choices)}")

                return choice

            except Exception as e:
                print(e)                
    

    def timer(self, seconds):
        for n in range(seconds, 0, -1):
            print(f"\rMemorize... {n}", end="")
            time.sleep(1)
        print()

    def clear_screen(self):
        os.system("cls" if os.name=="nt" else "clear")

    
    '''def level_up(self):

        if self.correct_answer >= 2:

            current_index = self.levels.index(self.level)

            if current_index < len(self.levels) - 1:
                self.level = self.levels[current_index + 1]
                print(f"\nLevel Up! Now you are in {self.level}")

            self.correct_answer = 0
            return True

        else:
            print("Sorry, you can't move to the next level. Try again.")
            self.correct_answer = 0
            return False'''

    def Secound_main(self,play_screen,practice_screen):

        menu_mood = '''
Choose mode: 
1- Play
2- Practice
3- Go back
'''

        while True:

            user_choice = input(menu_mood)

            match user_choice:

                case "1":
                    play_screen()

                case "2":
                    practice_screen()

                case "3":
                    print("Go back")
                    break

                case _:
                    print("Enter a valid number")
        