import time
import os
from colorama import Fore,Back

class Game:
    levels = ["Easy", "Medium", "Hard"]

    def __init__(self,username):
        self.username=username
        self.level = "Easy" 
        self._score = 0

    
    def set_score(self):
        self._score +=1

    def get_score(self):
        return self._score


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
        print(f"{Fore.BLUE}{name_of_game.center(35)}{Fore.RESET}")
        print("_"*35)
        print(f"{Fore.CYAN}Level:{Fore.RESET} {self.level}")
        print(f"{Back.GREEN}Score:{Back.RESET} {self._score}")
        if attempts is not None:
            print(f"{Fore.RED}Attempts Left: {Fore.RESET}{attempts}")
            print("-"*35)

   

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
        menu_level = f'''
{Fore.BLUE}Select a level: {Fore.RESET}
------------
{Fore.YELLOW}1{Fore.RESET} - Easy
{Fore.YELLOW}2{Fore.RESET} - Medium
{Fore.YELLOW}3{Fore.RESET} - Hard
{Fore.YELLOW}4{Fore.RESET} - Back 
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
                    return

                case _:
                    print(Fore.RED+"Enter a valid number"+Fore.RESET)

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
                    raise Exception(f"{Fore.RED}Please enter one of these: {Fore.RESET}{', '.join(valid_choices)}")

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
            print(f"\rTime left: {Fore.YELLOW}{n}{Fore.RESET}", end="")
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

        menu_mode = f'''
{Fore.BLUE}Select a mode{Fore.RESET}
------------
{Fore.YELLOW}1{Fore.RESET} - Play (Score will be saved)
{Fore.YELLOW}2{Fore.RESET} - Practice (Score will not be saved)
{Fore.YELLOW}3{Fore.RESET} - Back
'''

        while True:

            user_choice = input(menu_mode)

            match user_choice:

                case "1":
                    play_screen()

                case "2":
                    practice_screen()

                case "3":
                    return

                case _:
                    print("Enter a valid number")
        