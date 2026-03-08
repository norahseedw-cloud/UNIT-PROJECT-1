import time
import os

class Game:
    levels = ["Easy", "Medium", "Hard"]

    def __init__(self,username):
        self.username=username
        self.level = "Easy" 
        self.score = 0


    def display_header(self,name_of_game:str, attempts=None):
        """
    Displays the game header with the game name, level, score,
    and optionally the remaining attempts.
    ---------------
    name_of_game : str
        Name of the game shown in the header.
    attempts : int, optional
        Remaining attempts to display.
    """
        print("_"*35)
        print(name_of_game.center(35))
        print("_"*35)
        print(f"Level: {self.level}")
        print(f"Score: {self.score}")
        if attempts is not None:
            print(f"Attempts Left: {attempts}")
            print("-"*35)

    def correct(self):
        """
    Increases the player's score by one when the answer is correct.
    Then displays a confirmation message and the updated score.
    """
        self.score += 1
        print("Correct!")
        print(f"Score: {self.score}")

    def incorrect(self, attempts):
        """
    Displays a message for an incorrect answer and shows remaining attempts.
    ---------------
    attempts : int
        Number of attempts left.
    """
        print("Incorrect!")
        print(f"Attempts Left: {attempts}")

    def choose_level(self,easy_level,medium_level,hard_level):
        """
Displays a menu to choose a level and runs the selected level function.
---------------
easy_level : callable
    Function executed for Easy level.
medium_level : callable
    Function executed for Medium level.
hard_level : callable
    Function executed for Hard level.
"""
        menu_level = '''
Select a level:
1- Easy
2- Medium
3- Hard
4- Back 
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
        """
Gets input from the user and checks that it matches
one of the valid choices.
---------------
message : str
    The question shown to the user.
valid_choices : list
    Allowed user inputs.
"""

        while True:
            try:
                choice = input(message).strip().lower()

                if choice not in valid_choices:
                    raise Exception(f"Please enter one of these: {', '.join(valid_choices)}")

                return choice

            except Exception as e:
                print(e)                
    

    def timer(self, seconds):
        """
    This function displays a countdown timer for the user
    to memorize information before it disappears.
    ---------------
    seconds : int
        The number of seconds for the countdown.
    """
        for n in range(seconds, 0, -1):
            print(f"\rTime left: {n}", end="")
            time.sleep(1)
        print()

    def clear_screen(self):
        """
    This function clears the terminal screen depending
    on the operating system being used.
    """
        os.system("cls" if os.name=="nt" else "clear")



    def Secound_main(self,play_screen,practice_screen):
        """
Displays a menu to choose a mode and runs the selected function.
---------------
play_screen : callable
    Function executed for Play mode.
practice_screen : callable
    Function executed for Practice mode.
"""

        menu_mode = '''
Select a mode
------------
1- Play (Score will be saved)
2- Practice (Score will not be saved)
3- Back
'''

        while True:

            user_choice = input(menu_mode)

            match user_choice:

                case "1":
                    play_screen()

                case "2":
                    practice_screen()

                case "3":
                    break

                case _:
                    print("Enter a valid number")
        