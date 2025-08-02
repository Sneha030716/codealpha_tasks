import random
words = ['apple','robot','zebra','plant','stone']
word = random.choice(words)
hidden_word=['_'] * len(word)
wrong_guesses =0
max_guesses=6
guessed_letters=[]
print("welcome to Hangman!")
print("Guess the word letter by letter.")
while wrong_guesses<max_guesses and '_' in hidden_word:
    print("\nWord:",' '.join(hidden_word))
    guess=input("Enter a letter:").lower()

    if not guess.isalpha() or len(guess)!=1:
        print("Please enter a single letter:")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i]==guess:
                    hidden_word[i]=guess
    else:
        print("Wrong!")
        wrong_guesses+=1
        print(f"Remaining attempts:{max_guesses - wrong_guesses}")
if '_' not in hidden_word:
    print("\n you won! The word was:",word)
else:
    print("\n You lost! The word was:",word)
    
    
