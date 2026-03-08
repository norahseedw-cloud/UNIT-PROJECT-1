import json
import random
from games.base_game import Game
from storage import save_score


class StoryRecall(Game):

    def __init__(self, username):
        super().__init__(username)

        with open("games/stories.json", "r") as file:
            self.stories = json.load(file)


    def show_story(self, story):
        """
Displays the story for the player to memorize.
---------------
story : str
    The story shown to the player.
"""

        self.display_header("Story Recall")

        print("\nMemorize this story:\n")
        print(story)

        self.timer(8)
        self.clear_screen()


    def ask_questions(self, questions):
        """
Asks the player questions about the memorized story.
---------------
questions : list
    List of questions and their correct answers.
"""

        for q in questions:

            while True:

                self.display_header("Story Recall")

                answer = input(q["question"] + " ").strip().lower()

                if answer == "":
                    print("Answer cannot be empty!")
                    continue

                if answer.isdigit():
                    print("Please enter words only!")
                    continue

                break

            if answer == q["answer"].lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! Correct answer: {q['answer']}")

            input("\nPress Enter to continue...")
            self.clear_screen()


    def play_level(self, difficulty):
        """
Runs a round of the Story Recall game.
---------------
difficulty : str
    The selected difficulty level for the story.
"""

        self.score = 0

        while True:
            try:
                choice = input("Press Enter to start \n(Enter 0 to go back)\n> ")

                if choice == "":
                    break

                if choice == "0":
                    return

                raise ValueError("Please enter a valid input")

            except ValueError as e:
                print(e)

        round_number = 1

        while True:

            print(f"\n--- Round {round_number} ---")

            story_data = random.choice(self.stories[difficulty])

            story = story_data["story"]
            questions = story_data["questions"]

            self.show_story(story)

            self.ask_questions(questions)

            self.clear_screen()
            self.display_header("Story Recall")

            print(f"Your score: {self.score}\n")

            choice = self.get_choice("Play another round? (y/n):  ", ["y", "n"])

            if choice == "n":
                print(f"\nFinal score: {self.score}")
                save_score(self.username, "Story Recall", self.score,self.level)
                print("Thanks for playing!")
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

        print("--- Practice Mode ---")
        print("You will read a short story.")
        print("Try to remember the details.\n")
        while True:
            try:
                choice = input("Press Enter to start \n(Enter 0 to go back)\n ")

                if choice == "":
                    break

                if choice == "0":
                    return

                raise Exception("Please enter a valid input")

            except Exception as e:
                print(e)

        story_data = random.choice(self.stories["easy"])

        self.show_story(story_data["story"])

        self.ask_questions(story_data["questions"])

        print("Practice finished!")


    def display_game(self):

        self.choose_level(self.easy_level, self.medium_level, self.hard_level)


    def play(self):

        self.Secound_main(self.display_game, self.practice)


