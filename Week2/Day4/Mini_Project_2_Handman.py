
import random

# STEP 1: Choose a random word
wordslist = [
    'correction', 'childish', 'beach', 'python',
    'assertive', 'interference', 'complete',
    'share', 'credit card', 'rush', 'south'
]

word = random.choice(wordslist)

# STEP 2: Create the display word with stars
display_word = []

for letter in word:
    if letter == " ":
        display_word.append(" ")
    else:
        display_word.append("*")

# STEP 3: Create the gallows and game variables
gallows = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

mistakes = 0
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(display_word))


# STEP 4: Main game loop
while mistakes < 6 and "*" in display_word:

    guess = input("\nGuess a letter: ").lower()

    # Check if the player already guessed this letter
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    # Save the new guess
    guessed_letters.append(guess)

    # Check if the letter exists in the word
    if guess in word:

        print("Correct!")

        # Reveal all occurrences of the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")

        # Add one body part to the gallows
        print("You added:", gallows[mistakes])
        mistakes += 1

    # Display the current game status
    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", guessed_letters)
    print("Mistakes:", mistakes, "/ 6")


# STEP 5: Check the final result
if "*" not in display_word:
    print("\nCongratulations! You won!")

else:
    print("\nGame over! You lost!")
    print("The correct word was:", word)