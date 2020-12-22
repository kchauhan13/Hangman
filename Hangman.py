#User is asked to guess a letter, if it is part of the word,
#it is added, if not a letter is added to HANGMAN

from random_word import RandomWords
def split(word):
    return [char for char in word]
def checkword(guess):
    if guess == rand:
        print("You Win!")
        exit()
    global j, f
    if guess in word:
        print("Your guess is correct!")
        x = word.index(guess)
        a[x] = guess
        print(" ".join(a))
    elif not(guess in word):
        j += 1
        print("Your guess was incorrect\n Tries remaining: H" + "".join(trial[1:f]))
        return False
lines = open(

r = RandomWords()
rand = "genius"
trial = split("HANGMAN")
word = split(rand)
size = len(word)
a = []
j = 0
f = 1
for _ in range(size):
    a.append("_")

while (j != 7):
    guess = input("Guess a letter: ")
    if checkword(guess) is False:
        f +=1
    if "".join(a) == rand:
        print("You Win, Congratulations!")
        exit()
if j == 7:
    print("You Lose!")

