import random
from colorama import Fore,Back,Style
from games.base_game import Game
from storage import save_score
class NumberRecall(Game):

    def __init__(self, username):
        super().__init__(username)

    def generate_number(self, digits): 
        """
    This function generates a random number with a specific number
    of digits and displays it spaced out for the user to memorize.
    ---------------
    digits : int
        The number of digits to generate in the random number.
    """
        number = ""
        for _ in range(digits):
            number += str(random.randint(0, 9))

        self.number_to_remember = number

        display_number = " ".join(number)  # The space between numbers 
        print(f"\nRemember this number:\n{Fore.YELLOW}{display_number}{Fore.RESET}")


    def play_level(self, digits, attempts):
        """
    Runs a round of the Number Recall game.
    The player memorizes a number and tries to recall it.

    ---------------
    digits : int
        Number of digits in the generated number.
    attempts : int
        Number of attempts allowed for the player.
    """
        while True:
            try:
                choice = input(f"Press Enter to start \n{Fore.LIGHTRED_EX}(Enter 0 to go back){Fore.RESET}\n ")

                if choice == "":
                    break

                if choice == "0":
                    return

                raise ValueError(f"{Fore.RED}Please enter a valid input{Fore.RESET}")

            except ValueError as e:
                print(e)

        round_number = 1

        while True:

            print(f"\n{Fore.LIGHTCYAN_EX}--- Round {round_number} ---{Fore.RESET}")

            self.generate_number(digits)
            self.timer(5)
            self.clear_screen()

            attempts_left = attempts

            while attempts_left > 0:

                self.display_header("Number Recall", attempts_left)

                user_answer = input("Enter the number: ")

                if user_answer == self.number_to_remember:
                    print(Fore.GREEN + "Correct! ✅" + Fore.RESET)
                    self.set_score()
                    break

                attempts_left -= 1

                if attempts_left > 0:
                    print(Fore.RED + "Incorrect! Try again.. ❌" + Fore.RESET)
                else:
                    print(Fore.RED + "You have used all your attempts!" + Fore.RESET)
                    print(Fore.YELLOW + f"The correct number was {self.number_to_remember}" + Fore.RESET)

            print(f"{Fore.GREEN}Your score:{Fore.RESET} {self.get_score()}")

            choice = self.get_choice(f"{Fore.MAGENTA}Play another round? (y/n):{Fore.RESET} ", ["y", "n"])

            if choice == "n":
                print(f"\nFinal score: {self.get_score()}")
                save_score(self.username, "Number Recall", self.level,self.get_score())
                print(Fore.MAGENTA+Style.DIM+"Thanks for playing!"+Style.RESET_ALL)
                break

            round_number += 1


    def easy_level(self):
        self.level = "Easy"
        self.play_level(3, 3)  

    def medium_level(self):
        self.level = "Medium"
        self.play_level(5, 3)  


    def hard_level(self):
        self.level = "Hard"
        self.play_level(7, 3)   


    def practice(self):

        print(Fore.BLUE + "--- Practice Mode ---" + Fore.RESET)
        print(f''' {Fore.GREEN}
You will see a number for a few seconds.
Try to remember it and type it after the screen clears.
    {Fore.RESET}''')

        while True:
            try:
                choice = input(f"Press Enter to start \n{Fore.RED}(Enter 0 to go back)\n {Fore.RESET}")

                if choice == "":
                    break

                if choice == "0":
                    return

                raise Exception(Fore.RED + "Please enter a valid input" + Fore.RESET)

            except Exception as e:
                print(e)

        self.generate_number(3)
        self.timer(5)
        self.clear_screen()

        while True:
            try:
                user_answer = int(input("Enter the number: "))
                break

            except ValueError:
                print(Fore.RED + "Please enter numbers only!" + Fore.RESET)

        if str(user_answer) == self.number_to_remember:
            print(Fore.GREEN + "Correct! ✅" + Fore.RESET)
        else:
            print(Fore.RED + "Incorrect! ❌" + Fore.RESET)
            print(f"{Fore.YELLOW}The correct number was {self.number_to_remember}{Fore.RESET}")

        print(Fore.BLUE + Style.DIM + "Practice finished!" + Style.RESET_ALL)


    def display_game(self):
        self.choose_level(self.easy_level, self.medium_level, self.hard_level)


    def play(self):
        self.Secound_main(self.display_game, self.practice)


