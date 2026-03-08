import json
import os

FILE_NAME = "scores_of_users.json"

def save_score(username, game_name, level, score):

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    else:
        data = {}

    if username not in data:
        data[username] = {}

    if game_name not in data[username]:
        data[username][game_name] = {}

    data[username][game_name][level] = score

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def load_scores():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}