import random

hangman = ["""
 +---+
 O   |
/|\  |
/ \  |
    === ""","""
 +---+
 O   |
/|\  |
/    |
    === ""","""
 +---+
 O   |
/|\  |
     |
    === ""","""
 +---+
 O   |
/|   |
     |
    === ""","""
 +---+
 O   |
 |   |
     |
    === ""","""
 +---+
 O   |
     |
     |
    === ""","""
 +---+
     |
     |
     |
    === """]

words = ["python", "programming", "coding", "fun"]
target_word = random.choice(words)
guessed_word = ["_"] * len(target_word)

attempts = 6

while attempts > 0 and "_" in guessed_word:
    print(hangman[attempts+1])
    
    guess = input("Guess a letter: ")
    if guess in target_word:
        for i in range(len(target_word)):
            if target_word[i] == guess:
                guessed_word[i] = guess
        print("".join(guessed_word))
    else:
        attempts -= 1
        print(f"Wrong! You have {attempts} attempts left.")
    print("")
    print("--------------------")
    print("")


if "_" not in guessed_word:
    print("Congratulations! You guessed the word.")
else:
    print(f"Sorry, you're out of attempts. The word was {target_word}.")