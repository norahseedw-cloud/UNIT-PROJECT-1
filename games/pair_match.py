import random
from colorama import Back,Fore,Style
from games.base_game import Game
from storage import save_score

class PairMatch(Game):

    def __init__(self, username):
        super().__init__(username)

    def pairs(self, count):
        """
    This function generates letter-number pairs for the player to memorize.
    ---------------
count : int
        The number of pairs to generate.
    """
        letters = ["A", "B", "C", "D", "E"]
        selected_letters = letters[:count]

        numbers = [random.randint(0, 100) for _ in range(count)] # Random number
        self.pairs_dict = dict(zip(selected_letters, numbers)) # To add two together 

        for letter, number in self.pairs_dict.items():
            print(f"{Fore.YELLOW}{letter} -{Fore.RESET} {number}")


    def play_level(self, count):
        """
    Runs a round of the Pair Matching game.
    The player memorizes letter-number pairs and tries to recall them.
    ---------------
    count : int
        Number of letter-number pairs shown to the player.
    """
        while True:
            try:
                choice = input(f"Press Enter to start \n{Fore.RED}(Enter 0 to go back)\n{Fore.RESET} ")

                if choice == "":
                    break  

                if choice == "0":
                    return 

                raise ValueError(Fore.RED+"Please enter a valid input"+Fore.RESET)

            except ValueError as e:
                print(e)

        round_number = 1

        while True:

            print(f"{Fore.BLUE}\n--- Round {round_number} ---{Fore.RESET}")

            self.pairs(count)
            self.timer(5)
            self.clear_screen()

            attempts = 3
            correct_letters = {letter: False for letter in self.pairs_dict}

            while attempts > 0:

                self.display_header("Pair Matching", attempts)
                score_this_round = 0
                try:
                    for letter in self.pairs_dict:

                        if not correct_letters[letter]:

                            ask = int(input(f"What number was with {letter}: "))

                            if ask == self.pairs_dict[letter]:
                                print(f"{Fore.GREEN}{letter} is correct! ✅{Fore.RESET}")
                                correct_letters[letter] = True
                                score_this_round += 1
                            else:
                                print(f"{Fore.RED}{letter} is incorrect! ❌{Fore.RESET}")

                except ValueError:
                    print(Fore.RED+"Please enter numbers only!"+Fore.RESET)
                    continue

                for _ in range(score_this_round):
                 self.set_score()

                if all(correct_letters.values()):
                    print(Fore.GREEN+"All answers are correct! ✅"+Fore.RESET)
                    break

                attempts -= 1

                if attempts > 0:
                    print("Try again!")
                else:
                    print(Fore.RED + "You have used all your attempts!" + Fore.RESET)
                    for letter, number in self.pairs_dict.items():
                        print(f"{Fore.YELLOW}{letter}: {number}{Fore.RESET}")

            print(f"{Fore.GREEN}Your score:{Fore.RESET}{self.get_score()}")

            choice = self.get_choice(f"{Fore.MAGENTA}Play another round? (y/n):{Fore.RESET}  ", ["y", "n"])

            if choice == "n":
                print(f"\nFinal score: {self.get_score()}")
                save_score(self.username, "Pair Match", self.level,self.get_score())
                print(Fore.MAGENTA+Style.DIM+"Thanks for playing!"+Style.RESET_ALL)
                break

            round_number += 1

    def easy_level(self):
        self.level="Easy"
        self.play_level(2)

    def medium_level(self):
        self.level="Medium"
        self.play_level(3)

    def hard_level(self):
      self.level="Hard"
      self.play_level(4)   


    def practice(self):

        print(Fore.BLUE + "--- Practice Mode ---" + Fore.RESET)
        print(f''' {Fore.GREEN}
You will see letters with numbers for a few seconds.
Try to remember the number with each letter.
After the screen clears, type the correct number.
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

        self.pairs(2)
        self.timer(5)
        self.clear_screen()

        for letter in self.pairs_dict:

            while True:
                try:
                    ask = int(input(f"What number was with {letter}: "))
                    break

                except ValueError:
                    print(Fore.RED + "Please enter numbers only!" + Fore.RESET)

            if ask == self.pairs_dict[letter]:
                print(f"{Fore.GREEN}{letter} is correct! ✅{Fore.RESET}")
            else:
                print(f"{Fore.RED}{letter} is incorrect!{Fore.RESET}")
                print(f"{Fore.YELLOW}The correct number was {self.pairs_dict[letter]}{Fore.RESET}")

        print(Fore.BLUE + Style.DIM + "Practice finished!" + Style.RESET_ALL)

    def display_game(self):
        
        self.choose_level(self.easy_level, self.medium_level, self.hard_level)

    def play(self):
        self.Secound_main(self.display_game, self.practice)


