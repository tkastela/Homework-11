import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

new_score_list = sorted(score_list, key=lambda k: k['attempts'])

print("Top scores: ")
for i, player in enumerate(new_score_list[0:3]):
    print("{i + 1}. {player['player_name']}, attempts: {player['attempts']}")

player_name = input("Enter your name: ")

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number between 1 and 30: "))
    attempts = attempts + 1

    if guess == secret:
        score_list.append(
            {
                "player_name": player_name,
                "attempts": attempts,
                "date": str(datetime.datetime.now()),
                "wrong_guesses": attempts - 1,
                "secret_number": secret
            }
        )

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You have guessed it. It is number " + str(secret))
        print("Attempts needed" + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct. Try something smaller")
    elif guess < secret:
        print("Your guess is not correct. Try something bigger")

    wrong_guesses.append(guess)
