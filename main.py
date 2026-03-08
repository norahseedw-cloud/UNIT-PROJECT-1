from games.number_recall import NumberRecall
from games.pair_match import PairMatch
from games.category_recall import CategoryRecall
from games.story_recall import StoryRecall


username=input("Welcome to (game name) \n pleas enter your name: ").strip().lower()


number_recall_game = NumberRecall(username)
pair_match_game = PairMatch(username)
category_recall_game = CategoryRecall(username)
story_recall_game = StoryRecall(username)


def game_screen():

    
    menu = '''
Choose the game:
1-Number Recall
2-Pair Match
3-Category Recall
4-Story Recall
5-Back
'''

    while True:
        user_input = input(menu)

        match user_input:
            case "1":
                number_recall_game.play()

            case "2":
                pair_match_game.play()

            case "3":
                category_recall_game.play()

            case "4":
                story_recall_game.play()

            case "5":
                break

            case _:
                print("Enter a valid number")


menu = '''
Main menu:
1-Play games
2-View summary
3-Exit
'''


while True:
    user_choose = input(menu)

    match user_choose:
        case "1":
            game_screen()

        case "2":
            print("View summary")

        case "3":
            break

        case _:
            print("Enter a valid number")