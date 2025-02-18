import random

# Hangman stages
Stages = [
   
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """, """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ""","""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ""","""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ""","""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ""","""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ""","""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
    ]

word_list = ["horse","lion","elephant","eagle"]

# step-1:create a variable called "lives" to track the number of lives
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # step-2: if the guess is not a letter lives goes to the zero
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you win.")


    if "_" not in display:
        game_over = True
        print("You win.")

    # step-3: print the asci art from the stages

    print(Stages[lives])

    