from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"you got it! the answer was {actual_answer}")
        return 0


def set_difficulty():
    level = input("choose a dificulty . type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("invalid choice.please type 'easy' or 'hard' . ")


def game():
    print("welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint (1, 100)
    print(f"psst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("make a guess:  "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("guess again.")


game()

    



