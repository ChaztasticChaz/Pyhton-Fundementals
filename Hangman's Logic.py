import random

hangman = ["""
 +---+
 O   |
/|\  |
/ \  |if
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
guessed_letters = []

attempts = 6

while attempts > 0 and "_" in guessed_word:
    print(hangman[attempts])
    print("Letters guessed: " + str(guessed_word))
    print(guessed_letters)
    guess = input("Guess a letter: ")

    if guess in target_word:
        for i in range(len(target_word)):
            if target_word[i] == guess:
                guessed_word[i] = guess
        print("".join(guessed_word))
        guessed_letters.append(guess)
    else:
        attempts -= 1
        print(f"Sorry, {guess} is not apart of this word.")
        print(f"You have {attempts} attempts left.")
        guessed_letters.append(guess)
    
    print("")
    print("--------------------")
    print("")

#Checks if you have won or lost
if "_" not in guessed_word:
    print("Congratulations! You guessed the word.")
else:
    print(f"Sorry, you're out of attempts. The word was {target_word}.")
    print(hangman[0])