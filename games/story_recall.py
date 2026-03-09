import json
import random
from colorama import Back,Fore,Style
from games.base_game import Game
from storage import save_score


class StoryRecall(Game):

    def __init__(self, username):
        super().__init__(username)

        with open("games/stories.json", "r") as file:
            self.stories = json.load(file)


    def show_story(self, story, show_header=True):
        """
    Displays the story for the player to memorize.
    ---------------
    story : str
        The story shown to the player.
    """

        if show_header:
            self.display_header("Story Recall")

        print("\nMemorize this story:\n")
        print(story)

        self.timer(8)
        self.clear_screen()


    def ask_questions(self, questions, show_header=True):
        """
    Asks the player questions about the memorized story.
    ---------------
    questions : list
        List of questions and their correct answers.
    """

        for q in questions:

            attempts = 3

            while attempts > 0:

                if show_header:
                    self.display_header("Story Recall", attempts)

                answer = input(q["question"] + " ").strip().lower()

                if answer == "":
                    print(Fore.RED + "Answer cannot be empty!" + Fore.RESET)
                    continue

                if answer.isdigit():
                    print(Fore.RED + "Please enter words only!" + Fore.RESET)
                    continue

                if answer == q["answer"].lower():
                    print(Fore.GREEN + "Correct! ✅" + Fore.RESET)
                    self.set_score()
                    break

                attempts -= 1

                if attempts > 0:
                    print(Fore.RED + "Incorrect! Try again.. ❌" + Fore.RESET)
                else:
                    print(Fore.RED + "You have used all your attempts!" + Fore.RESET)
                    print(Fore.YELLOW + f"The correct answer was {q['answer']}" + Fore.RESET)

            while True:
                try:
                    play_again = input("\nPress Enter to continue... ")

                    if play_again != "":
                        raise ValueError(Fore.RED+"Please press Enter only!"+Fore.RESET)

                    break

                except ValueError as e:
                    print(Fore.RED + str(e) + Fore.RESET)
            self.clear_screen()


    def play_level(self, difficulty):
        """
Runs a round of the Story Recall game.
---------------
difficulty : str
    The selected difficulty level for the story.
"""

        self._score = 0

        while True:
            try:
                choice = input(f"Press Enter to start \n{Fore.RED}(Enter 0 to go back)\n{Fore.RESET} ")

                if choice == "":
                    break

                if choice == "0":
                    return

                raise ValueError(Fore.RED+"Please enter a valid input"+Fore.RED)

            except ValueError as e:
                print(e)

        round_number = 1

        while True:

            print(f"{Fore.BLUE}\n--- Round {round_number} ---{Fore.RESET}")

            story_data = random.choice(self.stories[difficulty])

            story = story_data["story"]
            questions = story_data["questions"]

            self.show_story(story)

            self.ask_questions(questions)

            self.clear_screen()
            self.display_header("Story Recall")

            print(f"{Fore.GREEN}Your score:{Fore.RESET} {self.get_score()}")

            choice = self.get_choice(f"{Fore.MAGENTA}Play another round? (y/n):{Fore.RESET} ", ["y", "n"])

            if choice == "n":
                print(f"\nFinal score: {self.get_score()}")
                save_score(self.username, "Story Recall", self.level,self.get_score())
                print(Fore.MAGENTA+Style.DIM+"Thanks for playing!"+Style.RESET_ALL)
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
You will read a short story.
Try to remember the details.
    {Fore.RESET}""")

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

        story_data = random.choice(self.stories["easy"])

        self.show_story(story_data["story"], False)
        self.ask_questions(story_data["questions"], False)

        print(Fore.BLUE + Style.DIM + "Practice finished!" + Style.RESET_ALL)


    def display_game(self):

        self.choose_level(self.easy_level, self.medium_level, self.hard_level)


    def play(self):

        self.Secound_main(self.display_game, self.practice)


