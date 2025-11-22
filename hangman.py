 
import random

words = ["apple", "banana", "computer", "python", "school"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = set()

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", " ".join(sorted(used_letters)))
    
    guess = input("Guess a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter one letter only.")
        continue
    if guess in used_letters:
        print("You already guessed that.")
        continue

    used_letters.add(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
