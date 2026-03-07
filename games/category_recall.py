import json
import random
from base_game import Game


class CategoryRecall(Game):

    def __init__(self):
        super().__init__()

        with open("games/categories.json", "r") as file:
            self.categories = json.load(file)


    def show_words(self, category, words):

        self.display_header("Category Recall")

        print(f"\nCategory: {category}\n")
        print("Memorize these words:\n")

        for word in words:
            print(word)

        self.timer(6)
        self.clear_screen()


    def ask_words(self, words):

        attempts = len(words)

        for i in range(len(words)):

            while True:

                self.display_header("Category Recall", attempts)

                answer = input("Name one word you remember: ").strip().lower()

                if answer == "":
                    print("Answer cannot be empty!")
                    continue

                if answer.isdigit():
                    print("Please enter words only!")
                    continue

                break

            if answer in words:
                print("Correct!")
                self.score += 1
                words.remove(answer)
            else:
                print("Wrong!")

            attempts -= 1


            while True:
                try:
                    play_again = input("\nPress Enter to continue... ")

                    if play_again != "":
                        raise ValueError("Please press Enter only!")

                    break

                except ValueError as e:
                    print(e)


    def play_level(self, difficulty):

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

            data = random.choice(self.categories[difficulty])

            category = data["category"]
            words = data["words"].copy()

            self.show_words(category, words)

            self.ask_words(words)

            self.clear_screen()
            self.display_header("Category Recall")

            print(f"Your score: {self.score}\n")

            choice = self.get_choice("Do you want another round? (y/n): ", ["y", "n"])

            if choice == "n":
                print(f"\nYour final score is: {self.score}")
                print("Thanks for playing! Goodbye.")
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
        print("You will see some words from a category.")
        print("Try to remember them.\n")

        data = random.choice(self.categories["easy"])

        self.show_words(data["category"], data["words"].copy())

        self.ask_words(data["words"].copy())

        print("Practice finished!")


    def display_game(self):

        self.choose_level(self.easy_level, self.medium_level, self.hard_level)


    def play(self):

        self.Secound_main(self.display_game, self.practice)


category_game = CategoryRecall()
category_game.play()




#الدزاين
#اعدل اسامي الدوال 
#اضافه كومنت 
#اضافه كاتقوىي مع الهيدر