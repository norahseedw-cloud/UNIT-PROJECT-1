import json
import random
from colorama import Fore, Back, Style
from games.base_game import Game
from storage import save_score


class CategoryRecall(Game):

    def __init__(self, username):
        super().__init__(username)

        with open("games/categories.json", "r") as file:
            self.categories = json.load(file)


    def show_words(self, category, words, show_header=True):
        """
    Displays the category and words for the player to memorize.
    ---------------
    category : str
        The category shown to the player.
    words : list
        Words related to the category to memorize.
    """

        if show_header:
            self.display_header("Category Recall")

        print(f"\n{Fore.YELLOW}Category:{Fore.RESET} {category}\n")
        print("Memorize these words:\n")

        for word in words:
            print(word)

        self.timer(5)
        self.clear_screen()


    def ask_words(self, words, show_header=True):
        """
Asks the player to recall words from the memorized list.
---------------
words : list
        The list of words the player should remember.
    """

        original_words = words.copy()
        attempts = 3

        while attempts > 0:

            if show_header:
                self.display_header("Category Recall", attempts)

            answer = input("Name one word you remember: ").strip().lower()

            if answer == "":
                print(Fore.RED + "Answer cannot be empty!" + Fore.RESET)
                continue

            if answer.isdigit():
                print(Fore.RED + "Please enter words only!" + Fore.RESET)
                continue

            if answer in words:
                print(Fore.GREEN + "Correct! ✅" + Fore.RESET)
                self.set_score()
                words.remove(answer)

            elif answer in original_words:
                print(Fore.YELLOW + "You already used this word!" + Fore.RESET)

            else:
                attempts -= 1

                if attempts > 0:
                    print(Fore.RED + "Incorrect! Try again.." + Fore.RESET)
                else:
                    print(Fore.RED + "You have used all your attempts!" + Fore.RESET)

            if not words:
                break

            while True:
                try:
                    play_again = input("\nPress Enter to continue... ")

                    if play_again != "":
                        raise ValueError("Please press Enter only!")

                    break

                except ValueError as e:
                    print(Fore.RED + str(e) + Fore.RESET)


    def play_level(self, difficulty):
        """
Runs a round of the Category Recall game.
---------------
difficulty : str
    The selected difficulty level for the game.
"""

        self._score = 0

        while True:
            try:
                choice = input(
                    f"Press Enter to start \n{Fore.RED}(Enter 0 to go back)\n{Fore.RESET} "
                )

                if choice == "":
                    break

                if choice == "0":
                    return

                raise ValueError(Fore.RED + "Please enter a valid input" + Fore.RESET)

            except ValueError as e:
                print(e)

        round_number = 1

        while True:

            print(f"{Fore.BLUE}\n--- Round {round_number} ---{Fore.RESET}")

            data = random.choice(self.categories[difficulty])

            category = data["category"]
            words = data["words"].copy()

            self.show_words(category, words)

            self.ask_words(words)

            self.clear_screen()
            self.display_header("Category Recall")

            print(f"{Fore.GREEN}Your score:{Fore.RESET} {self.get_score()}\n")

            choice = self.get_choice(
                f"{Fore.MAGENTA}Play another round? (y/n):{Fore.RESET} ",
                ["y", "n"]
            )

            if choice == "n":

                print(f"\nFinal score: {self.get_score()}")

                save_score(
                    self.username,
                    "Category Recall",
                    self.level,
                    self.get_score()
                )

                print(Fore.MAGENTA + Style.DIM + "Thanks for playing!" + Style.RESET_ALL)

                break

            round_number += 1


    def easy_level(self):
        self.level = "Easy"
        self.play_level("easy")


    def medium_level(self):
        self.level = "Medium"
        self.play_level("medium")


    def hard_level(self):
        self.level = "Hard"
        self.play_level("hard")


    def practice(self):

        print(Fore.BLUE + "--- Practice Mode ---" + Fore.RESET)

        print(f"""{Fore.GREEN}
You will see some words from a category.
Try to remember them.
{Fore.RESET}""")

        while True:
            try:
                choice = input(
                    f"Press Enter to start \n{Fore.RED}(Enter 0 to go back)\n {Fore.RESET}"
                )

                if choice == "":
                    break

                if choice == "0":
                    return

                raise Exception(Fore.RED + "Please enter a valid input" + Fore.RESET)

            except Exception as e:
                print(e)

        data = random.choice(self.categories["easy"])

        self.show_words(data["category"], data["words"].copy(),False)

        self.ask_words(data["words"].copy(),False)

        print(Fore.BLUE + Style.DIM + "Practice finished!" + Style.RESET_ALL)


    def display_game(self):

        self.choose_level(self.easy_level, self.medium_level, self.hard_level)


    def play(self):

        self.Secound_main(self.display_game, self.practice)