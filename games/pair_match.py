import random
from base_game import Game


class PairMatch(Game):



    def pairs(self):
        letters = ["A","B","C"]
        numbers = [random.randint(0,100) for _ in range(3)]

        self.pairs_dict = dict(zip(letters, numbers))

        for letter, number in self.pairs_dict.items():
            print(f"{letter} - {number}")

   




    def play_pair_match(self):
        self.pairs()
        self.timer(5)
        self.clear_screen()

        ask_for_answer = int(input("What was with A: "))
        """  try:
            if not ask_for_answer:
                raise Exception("The answer can't be empty")

            if not ask_for_answer.isdigit():
                raise Exception("The answer must be numbers only")

            if len(ask_for_answer) != digits_level:
                raise Exception(f"The answer must be exactly {digits_level} numbers")

        except Exception as e:
            print(e)"""
            
        

        if ask_for_answer == self.pairs_dict["A"]:
            self.correct()
        else:
            self.incorrect(3)
            
       


    def display_game(self):
        print("_"*35)
        print("Pair Matching".center(35))
        print("_"*35)
        self.display_header(3)
        print("-"*35)
        print("Memorize the pairs: ")
        self.play_pair_match()
        


    def play(self):
        self.Secound_main(self.display_game, self.display_game)





pair_match1=PairMatch()

pair_match1.play()